"""Výpočty finančnej analýzy podľa M. Synka (Ekonomická analýza) pre COOP Jednota Čadca."""
import math
from data import YEARS, AKTIVA as A, PASIVA as P, VZAS as V, CASHFLOW as CF, KPI

n = len(YEARS)


def s(d, *keys):
    return [sum(d[k][i] for k in keys) for i in range(n)]


# --- Medzisúčty z výsledovky -------------------------------------------------
T = s(V, "r03", "r04", "r05")                 # tržby (tovar + výrobky + služby)
EAT = V["r61"]
EBT = V["r56"]                                # = EAT + daň (r57) + prevod podielov (r60)
EBIT = [EBT[i] + V["r49"][i] for i in range(n)]
EBITDA = [EBIT[i] + V["r21"][i] for i in range(n)]
VYNOSY = s(V, "r02", "r29")
NAKLADY = [VYNOSY[i] - EAT[i] for i in range(n)]   # vrátane dane
OBCH_MARZA = [V["r03"][i] - V["r11"][i] for i in range(n)]

# --- Súvahové agregáty -------------------------------------------------------
AK = A["r01"]
VK = P["r80"]
CZ = P["r101"]                                # cudzie zdroje (záväzky + rezervy + úvery)
KZ = s(P, "r122", "r139", "r140")             # krátkodobé záväzky + bežné úvery + KFV
DCZ = s(P, "r102", "r118", "r121")            # dlhodobé cudzie zdroje
FM = s(A, "r66", "r71")                       # finančný majetok
OM = [A["r33"][i] - A["r41"][i] for i in range(n)]   # obežný majetok bez dlhodobých pohľadávok
KP = A["r53"]
ZAS = A["r34"]
CPK = [OM[i] - KZ[i] for i in range(n)]
CF_QT = [EAT[i] + V["r21"][i] for i in range(n)]     # zjednodušený CF = EAT + odpisy

R = {}
R["ROE"] = [EAT[i] / VK[i] for i in range(n)]
R["ROA"] = [EBIT[i] / AK[i] for i in range(n)]
R["ROS"] = [EAT[i] / T[i] for i in range(n)]
R["ROCE"] = [EBIT[i] / (VK[i] + DCZ[i]) for i in range(n)]
R["EBITDA marža"] = [EBITDA[i] / T[i] for i in range(n)]
R["Obchodná marža"] = [OBCH_MARZA[i] / V["r03"][i] for i in range(n)]
R["L1 okamžitá"] = [FM[i] / KZ[i] for i in range(n)]
R["L2 pohotová"] = [(FM[i] + KP[i]) / KZ[i] for i in range(n)]
R["L3 bežná"] = [OM[i] / KZ[i] for i in range(n)]
R["ČPK"] = CPK
R["Obrat aktív"] = [T[i] / AK[i] for i in range(n)]
R["Obrat zásob"] = [T[i] / ZAS[i] for i in range(n)]
R["DO zásob (dni)"] = [ZAS[i] / (T[i] / 360) for i in range(n)]
R["DO pohľadávok (dni)"] = [A["r54"][i] / (T[i] / 360) for i in range(n)]
R["DO záväzkov (dni)"] = [P["r123"][i] / (T[i] / 360) for i in range(n)]
R["Celková zadlženosť"] = [CZ[i] / AK[i] for i in range(n)]
R["Koef. samofinancovania"] = [VK[i] / AK[i] for i in range(n)]
R["Miera zadlženia CZ/VK"] = [CZ[i] / VK[i] for i in range(n)]
R["Finančná páka A/VK"] = [AK[i] / VK[i] for i in range(n)]
R["Úrokové krytie"] = [EBIT[i] / V["r49"][i] for i in range(n)]
R["Krytie DM VK"] = [VK[i] / A["r02"][i] for i in range(n)]
R["Tržby na zamestnanca"] = [T[i] / KPI["zamestnanci"][i] for i in range(n)]
R["PH na zamestnanca"] = [V["r28"][i] / KPI["zamestnanci"][i] for i in range(n)]
R["Priem. mesačná mzda"] = [V["r16"][i] / KPI["zamestnanci"][i] / 12 for i in range(n)]

# --- Du Pont ROE + logaritmická metóda ---------------------------------------
DUPONT = {
    "Daňová redukcia EAT/EBT": [EAT[i] / EBT[i] for i in range(n)],
    "Úroková redukcia EBT/EBIT": [EBT[i] / EBIT[i] for i in range(n)],
    "Prevádzková rentabilita EBIT/T": [EBIT[i] / T[i] for i in range(n)],
    "Obrat aktív T/A": [T[i] / AK[i] for i in range(n)],
    "Finančná páka A/VK": [AK[i] / VK[i] for i in range(n)],
}


def log_rozklad(factors, y):
    """Logaritmická metóda: Δy_ai = ln(I_ai) / ln(I_y) · Δy."""
    out = []
    for i in range(1, n):
        dy = y[i] - y[i - 1]
        ly = math.log(y[i] / y[i - 1])
        infl = {k: math.log(v[i] / v[i - 1]) / ly * dy for k, v in factors.items()}
        out.append((YEARS[i - 1], YEARS[i], dy, infl))
    return out


ROE_LOG = log_rozklad(DUPONT, R["ROE"])

DUPONT_ROA = {
    "EBIT/T": DUPONT["Prevádzková rentabilita EBIT/T"],
    "T/A": DUPONT["Obrat aktív T/A"],
}
ROA_LOG = log_rozklad(DUPONT_ROA, R["ROA"])

# --- Altman Z′ (1983, nekótované firmy) --------------------------------------
X1 = [CPK[i] / AK[i] for i in range(n)]
X2 = [(P["r97"][i] + P["r100"][i]) / AK[i] for i in range(n)]
X2b = [(P["r90"][i] + P["r97"][i] + P["r100"][i]) / AK[i] for i in range(n)]
X3 = [EBIT[i] / AK[i] for i in range(n)]
X4 = [VK[i] / CZ[i] for i in range(n)]
X5 = [T[i] / AK[i] for i in range(n)]
Z = [0.717 * X1[i] + 0.847 * X2[i] + 3.107 * X3[i] + 0.420 * X4[i] + 0.998 * X5[i] for i in range(n)]
Zb = [0.717 * X1[i] + 0.847 * X2b[i] + 3.107 * X3[i] + 0.420 * X4[i] + 0.998 * X5[i] for i in range(n)]


def z_pasmo(z):
    return "pásmo prosperity" if z > 2.9 else ("šedá zóna" if z >= 1.23 else "pásmo bankrotu")


# --- Quick test (Kralicek) ---------------------------------------------------
def znamka(v, hranice, rastuce=True):
    # hranice pre známky 1..4; inak 5
    for z, h in enumerate(hranice, start=1):
        if (v > h if rastuce else v < h):
            return z
    return 5


QT = []
for i in range(n):
    r1 = VK[i] / AK[i]
    r2 = (CZ[i] - FM[i]) / CF_QT[i]
    r3 = CF_QT[i] / T[i]
    r4 = EBIT[i] / AK[i]
    z1 = znamka(r1, [0.30, 0.20, 0.10, 0.0])
    z2 = znamka(r2, [3, 5, 12, 30], rastuce=False) if r2 >= 0 else 1
    z3 = znamka(r3, [0.10, 0.08, 0.05, 0.0])
    z4 = znamka(r4, [0.15, 0.12, 0.08, 0.0])
    fs = (z1 + z2) / 2
    vs = (z3 + z4) / 2
    QT.append(dict(r1=r1, r2=r2, r3=r3, r4=r4, z=(z1, z2, z3, z4), fs=fs, vs=vs, total=(fs + vs) / 2))


def horiz(vals):
    return [(vals[i] - vals[i - 1], vals[i] / vals[i - 1]) for i in range(1, n)]


if __name__ == "__main__":
    def row(name, vals, fmt="{:>14,.0f}"):
        print(f"{name:32s}" + "".join(fmt.format(v) for v in vals))

    print(" " * 32 + "".join(f"{y:>14}" for y in YEARS))
    for nm, v in [("Aktíva", AK), ("Neobežný majetok", A["r02"]), ("Obežný majetok", A["r33"]),
                  ("Zásoby", ZAS), ("Fin. účty", FM), ("Vlastné imanie", VK), ("Cudzie zdroje", CZ),
                  ("Krátkodobé záväzky", KZ), ("Tržby T", T), ("Výnosy spolu", VYNOSY),
                  ("Náklady spolu (vr. dane)", NAKLADY), ("NOPT", V["r11"]), ("Obchodná marža", OBCH_MARZA),
                  ("Energie+materiál", V["r12"]), ("Osobné náklady", V["r15"]), ("Odpisy", V["r21"]),
                  ("PH", V["r28"]), ("EBITDA", EBITDA), ("EBIT", EBIT), ("EBT", EBT), ("EAT", EAT),
                  ("CF (EAT+odpisy)", CF_QT), ("CF prevádzka", CF["CF_prevadzka"]), ("Capex", CF["capex"])]:
        row(nm, v)
    print("\nHorizontálna analýza (index)")
    for nm, v in [("Aktíva", AK), ("VK", VK), ("CZ", CZ), ("Tržby", T), ("Výnosy", VYNOSY), ("Náklady", NAKLADY),
                  ("Osobné n.", V["r15"]), ("Energie", V["r12"]), ("EBIT", EBIT), ("EAT", EAT), ("Zásoby", ZAS),
                  ("DHM", A["r11"]), ("Fin. účty", FM), ("Obch. záväzky", P["r123"])]:
        print(f"{nm:32s}" + " " * 14 + "".join(f"{ix:>14.4f}" for d, ix in horiz(v)))
    print("\nVertikálna analýza (% aktív / % tržieb)")
    for nm, v in [("Neobežný", A["r02"]), ("Obežný", A["r33"]), ("Zásoby", ZAS), ("FM", FM), ("VK", VK), ("CZ", CZ), ("KZ", KZ)]:
        row(nm, [v[i] / AK[i] * 100 for i in range(n)], "{:>14.2f}")
    for nm, v in [("NOPT", V["r11"]), ("Osobné", V["r15"]), ("Energie", V["r12"]), ("Služby", V["r14"]), ("Odpisy", V["r21"]), ("EAT", EAT)]:
        row(nm + " / T", [v[i] / T[i] * 100 for i in range(n)], "{:>14.2f}")
    print("\nPomerové ukazovatele")
    for k, v in R.items():
        row(k, v, "{:>14,.4f}" if abs(v[0]) < 1000 else "{:>14,.0f}")
    print("\nDu Pont ROE")
    for k, v in DUPONT.items():
        row(k, v, "{:>14.5f}")
    row("ROE", R["ROE"], "{:>14.5f}")
    print("\nLogaritmický rozklad ΔROE (v p.b.)")
    for y0, y1, dy, infl in ROE_LOG:
        print(f"{y0}/{y1}: ΔROE={dy*100:+.3f} p.b. | " + " | ".join(f"{k.split()[0]} {v*100:+.3f}" for k, v in infl.items()) + f" | Σ={sum(infl.values())*100:+.3f}")
    print("\nLogaritmický rozklad ΔROA (v p.b.)")
    for y0, y1, dy, infl in ROA_LOG:
        print(f"{y0}/{y1}: ΔROA={dy*100:+.3f} | " + " | ".join(f"{k} {v*100:+.3f}" for k, v in infl.items()))
    print("\nAltman Z′")
    for nm, v in [("X1", X1), ("X2", X2), ("X2b (s fondmi)", X2b), ("X3", X3), ("X4", X4), ("X5", X5), ("Z′", Z), ("Z′ (X2b)", Zb)]:
        row(nm, v, "{:>14.4f}")
    print("  " + ", ".join(f"{y}: {z_pasmo(z)}" for y, z in zip(YEARS, Z)))
    print("\nQuick test")
    for y, q in zip(YEARS, QT):
        print(y, {k: (round(v, 4) if isinstance(v, float) else v) for k, v in q.items()})
