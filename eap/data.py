"""Údaje z účtovných závierok COOP Jednota Čadca, s.d. (IČO 00168947), v celých EUR.
Zdroj: výročné správy 2022 a 2024 (stĺpce bežné/bezprostredne predchádzajúce obdobie),
overené proti VS 2023. Súvaha Úč POD 1-01 (Netto), VZaS Úč POD 2-01.
Kľúč = číslo riadku výkazu."""

YEARS = [2021, 2022, 2023, 2024]

# Súvaha – strana aktív (Netto)
AKTIVA = {
    "r01": [29419784, 33187123, 36332737, 38041118],  # SPOLU MAJETOK
    "r02": [18690703, 20227478, 21913940, 23554699],  # A. Neobežný majetok
    "r03": [50873, 30410, 31870, 14394],              # A.I. DNM
    "r11": [17863424, 18625337, 20093105, 21864810],  # A.II. DHM
    "r12": [1011532, 1146595, 1200475, 1602124],      # pozemky
    "r13": [11681091, 12927904, 13926631, 14686835],  # stavby
    "r14": [3355945, 4042638, 4420242, 4301707],      # hnuteľné veci
    "r17": [359660, 359845, 348269, 336694],          # ostatný DHM
    "r18": [1455196, 148355, 197488, 937450],         # obstarávaný DHM
    "r21": [776406, 1571731, 1788965, 1675495],       # A.III. DFM
    "r33": [10688515, 12758323, 14336467, 14418386],  # B. Obežný majetok
    "r34": [6286514, 7859138, 8643059, 8784147],      # B.I. Zásoby
    "r35": [73117, 104912, 130026, 103378],           # materiál
    "r39": [6208750, 7749579, 8508386, 8676122],      # tovar
    "r41": [300111, 418650, 349936, 423735],          # B.II. Dlhodobé pohľadávky (odložená daň)
    "r53": [1597977, 1886949, 2382211, 1791221],      # B.III. Krátkodobé pohľadávky
    "r54": [1356918, 1825570, 2004451, 1730911],      # z obchodného styku
    "r63": [171778, 118, 318527, 8894],               # daňové pohľadávky
    "r65": [69281, 61261, 59233, 51416],              # iné pohľadávky
    "r66": [0, 0, 0, 0],                              # B.IV. KFM
    "r71": [2503913, 2593586, 2961261, 3419283],      # B.V. Finančné účty
    "r72": [551116, 719798, 796524, 644894],          # peniaze
    "r73": [1952797, 1873788, 2164737, 2774389],      # účty v bankách
    "r74": [40566, 201322, 82330, 68033],             # C. Časové rozlíšenie
}

# Súvaha – strana pasív
PASIVA = {
    "r79": [29419784, 33187123, 36332737, 38041118],  # SPOLU VI A ZÁVÄZKY
    "r80": [15661836, 18269736, 21780695, 24136130],  # A. Vlastné imanie
    "r81": [1120761, 1119656, 1119061, 1118432],      # A.I. Základné imanie
    "r85": [0, 0, 0, 0],
    "r86": [0, 0, 0, 0],
    "r87": [3965001, 3965001, 3965001, 3965001],      # A.IV. Zákonné rezervné (nedeliteľné) fondy
    "r90": [9048705, 10043027, 11865361, 15145664],   # A.V. Ostatné fondy zo zisku
    "r93": [236673, 1031998, 1249231, 1135762],       # A.VI. Oceňovacie rozdiely
    "r97": [212902, 213138, 213367, 213620],          # A.VII. VH minulých rokov
    "r100": [1077794, 1896916, 3368674, 2557651],     # A.VIII. VH bežného obdobia
    "r101": [13751049, 14913342, 14489977, 13852489], # B. Záväzky (cudzie zdroje)
    "r102": [887636, 985882, 1047947, 1260725],       # B.I. Dlhodobé záväzky
    "r114": [128810, 139322, 134405, 120654],         # sociálny fond
    "r117": [758826, 846560, 913542, 1140071],        # odložený daňový záväzok
    "r118": [188820, 244198, 177609, 209279],         # B.II. Dlhodobé rezervy
    "r121": [0, 0, 0, 0],                             # B.III. Dlhodobé bankové úvery
    "r122": [10972887, 11679850, 11466765, 10515919], # B.IV. Krátkodobé záväzky
    "r123": [8721084, 9134127, 8683080, 7742215],     # z obchodného styku
    "r130": [45552, 50502, 55103, 59940],             # voči spoločníkom/členom
    "r131": [893328, 860944, 1036859, 1106106],       # voči zamestnancom
    "r132": [594129, 583327, 677721, 741982],         # sociálne poistenie
    "r133": [697749, 1029441, 990244, 838532],        # daňové záväzky
    "r135": [21045, 21509, 23758, 27144],             # iné záväzky
    "r136": [1701706, 2003412, 1797656, 1866566],     # B.V. Krátkodobé rezervy
    "r139": [0, 0, 0, 0],                             # B.VI. Bežné bankové úvery
    "r140": [0, 0, 0, 0],                             # B.VII. Krátkodobé finančné výpomoci
    "r141": [6899, 4045, 62065, 52499],               # C. Časové rozlíšenie
}

# Výkaz ziskov a strát
VZAS = {
    "r01": [112659445, 123556842, 136383734, 142738351],  # Čistý obrat
    "r02": [112745242, 123701349, 137912147, 142979491],  # Výnosy z hosp. činnosti spolu
    "r03": [110938616, 121390797, 133508655, 140037980],  # Tržby z predaja tovaru
    "r04": [0, 0, 0, 0],                                  # Tržby z predaja vlastných výrobkov
    "r05": [1720829, 2166045, 2875079, 2700371],          # Tržby z predaja služieb
    "r08": [19475, 5833, 15000, 85000],                   # Tržby z predaja DM a materiálu
    "r09": [66322, 138674, 1513413, 156140],              # Ostatné výnosy z HČ
    "r10": [111266762, 121352439, 133993178, 139655105],  # Náklady na HČ spolu
    "r11": [85452353, 93053014, 101422432, 106928808],    # Náklady na obstaranie predaného tovaru
    "r12": [2793922, 3606881, 6315007, 3926537],          # Spotreba materiálu a energie
    "r13": [0, 0, 0, 0],
    "r14": [3212783, 3342774, 3645617, 3937852],          # Služby
    "r15": [17756580, 18932138, 20288028, 22193022],      # Osobné náklady
    "r16": [12204790, 12811983, 13921709, 15016894],      # Mzdové náklady
    "r20": [156875, 160984, 170405, 213743],              # Dane a poplatky
    "r21": [1448283, 1640209, 1733942, 1793017],          # Odpisy
    "r24": [7176, 0, 0, 51],                              # ZC predaného DM
    "r25": [0, 0, 0, 0],
    "r26": [438790, 616439, 417747, 662075],              # Ostatné náklady na HČ
    "r27": [1478480, 2348910, 3918969, 3324386],          # VH z hospodárskej činnosti
    "r28": [21200387, 23554173, 25000678, 27945154],      # Pridaná hodnota
    "r29": [192567, 344108, 638509, 411884],              # Výnosy z finančnej činnosti
    "r39": [0, 0, 0, 31182],                              # Výnosové úroky
    "r45": [296181, 338355, 410443, 424722],              # Náklady na finančnú činnosť
    "r49": [283, 270, 999, 707],                          # Nákladové úroky
    "r55": [-103614, 5753, 228066, -12838],               # VH z finančnej činnosti
    "r56": [1374866, 2354663, 4147035, 3311548],          # VH pred zdanením
    "r57": [297072, 457747, 778361, 753897],              # Daň z príjmov
    "r60": [0, 0, 0, 0],                                  # Prevod podielov na VH
    "r61": [1077794, 1896916, 3368674, 2557651],          # VH po zdanení
}

# Prehľad peňažných tokov (poznámky, čl. X)
CASHFLOW = {
    "CF_prevadzka": [2517290, 1410677, 2782727, 3747190],
    "CF_investicie": [-3396799, -2031718, -2556338, -3086245],
    "capex": [-3608841, -2381659, -3203237, -3551423],
}

# Nefinančné údaje z výročných správ
KPI = {
    "MOO_eur": [131340000, 143474000, 157654501, 165401404],  # maloobchodný obrat s DPH
    "zamestnanci": [1025, 1013, 1005, 1006],                   # priemerný prepočítaný stav
}
