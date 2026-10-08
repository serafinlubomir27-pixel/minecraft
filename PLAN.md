# Plán semestrálnej práce – EAP (VŠB-TUO), ZS 2026/2027

**Analyzovaná spoločnosť:** COOP Jednota Čadca, spotrebné družstvo (IČO 00168947, Palárikova 87, 022 01 Čadca)
**Obdobie:** 2021 – 2025
**Termín odovzdania do LMS:** 19. 12. 2026
**Metodika:** M. Synek – *Ekonomická analýza*; slovenské postupy účtovania (Opatrenie MF SR č. MF/23377/2014-74, výkazy Úč POD)

---

## 0. Čo už vieme (verejné zdroje)

| Údaj | Hodnota | Zdroj |
|---|---|---|
| Tržby 2025 | ≈ 149,8 mil. € (+5 % r/r) | FinStat |
| Výnosy spolu 2025 | 150 576 076 € | FinStat |
| Zisk 2025 | ≈ 2,405 mil. € (−6 % r/r) | FinStat |
| Aktíva spolu 2025 | 40 752 585 € | FinStat |
| Počet predajní | 132 (12 Tempo SUPERMARKET, 56 SUPERMARKET, 65 POTRAVINY) | coopcadca.sk |
| Zamestnanci | > 1 000 | coopcadca.sk, FinStat |
| Región | okresy CA, KNM, ZA, PB, IL, PU, TN, NM n. V. | coopcadca.sk |
| Maloobchodný obrat 2023 | 157,65 mil. € (s DPH) | VS COOP Jednota Slovensko 2023 |
| Skupina COOP Jednota 2024 | tržby 1,767 mld. € (+4,0 %) | coop.sk |

Tieto čísla použijeme **iba na kontrolu**. Výpočty robíme výhradne z úplných účtovných závierok (súvaha, VZaS, poznámky, výročné správy).

**Makro a sektor (do Úvodu):**
- 2021: dozvuky COVID-19, obmedzenia prevádzok, nákup v blízkych obchodoch pomáhal sieťam typu COOP.
- 2022 – 2023: energetická kríza a dvojciferná inflácia (potraviny > 20 %), prudký rast cien energií a miezd. Reálne tržby klesali, nominálne rástli.
- 2024: dezinflácia, oživenie reálnej spotreby.
- 2025: konsolidačný balík (DPH 23 %, potraviny 19 %, základné potraviny 5 %), transakčná daň od 4/2025, rast minimálnej mzdy. Podľa SAMO tržby potravinového maloobchodu +3,4 %, potraviny +3,1 %; obchodníci tlmili ceny na úkor marží.
- Konkurencia: Lidl, Kaufland, Tesco, Billa a diskonty; demografický odliv z Kysúc.

---

## 1. Fáza – Zber dát (ČAKÁ NA VÁS)

Potrebujeme od vás:
1. **Súvahu** (Aktíva + Pasíva) za 2021 – 2025. Stačia stĺpce „Bežné účtovné obdobie – Netto“ a „Bezprostredne predchádzajúce obdobie“. Postačia závierky 2022, 2024 a 2025, lebo každá obsahuje aj predchádzajúci rok.
2. **Výkaz ziskov a strát** 2021 – 2025 (všetky riadky 01 – 61).
3. **Cash-flow**, ak ho družstvo zostavuje. Ak nie, CF dopočítame nepriamou metódou (EAT + odpisy ± zmena pracovného kapitálu). Potrebujeme ho pre Quick test.
4. **Výročné správy** 2021 – 2025: počet predajní, investície, zamestnanci, udalosti.
5. **Excel šablónu z LMS**, aby výpočty presne sedeli s jej riadkami.
6. **Odkaz**, ktorý ste spomínali. V správe nebol, pošlite ho znova.

**Formát:** PDF z registeruz.sk / finstat.sk, fotky, CSV alebo hodnoty prepísané do tabuľky. Všetko v celých eurách.

> ⚠️ **Overiť s vyučujúcim:** zadanie hovorí o firme z českého obchodného rejstříku (or.justice.cz). COOP Jednota Čadca je zapísaná v slovenskom ORSR (Okresný súd Žilina) a závierky má v registeruz.sk. Odporúčame potvrdiť, že slovenská firma je akceptovaná.

---

## 2. Fáza – Výpočty (Excel)

| Krok | Obsah | Poznámka k metodike |
|---|---|---|
| 2.1 | Prepis výkazov do šablóny | mapovanie riadkov SK súvahy (r. 001 – 145) a VZaS (r. 01 – 61) |
| 2.2 | **Horizontálna analýza** | absolútna zmena Δ = Xₜ − Xₜ₋₁; reťazový index Iₜ = Xₜ / Xₜ₋₁ |
| 2.3 | **Vertikálna analýza** | súvaha: podiel na aktívach / pasívach spolu; VZaS: podiel na tržbách (resp. výnosoch) |
| 2.4 | **Výsledovkové medzisúčty** (VZaS Úč POD 2014) | EAT = r. 61; EBT = r. 56 (= EAT + daň z príjmov r. 57 + prevod podielov r. 60); EBIT = EBT + nákladové úroky r. 49. Riadky overíme podľa vašich výkazov. |
| 2.5 | **Pomerové ukazovatele** | ROE, ROA, ROS, ROCE; L1, L2, L3, ČPK; obrat aktív, obrat a doba obratu zásob, pohľadávok, záväzkov; celková zadlženosť, koeficient samofinancovania, finančná páka, úrokové krytie |
| 2.6 | **Du Pont ROE** | ROE = (EAT/EBT) · (EBT/EBIT) · (EBIT/T) · (T/A) · (A/VK) |
| 2.7 | **Logaritmická metóda** | vplyv faktora aᵢ: Δx_aᵢ = (ln I_aᵢ / ln I_x) · Δx; pre každú dvojicu rokov 21/22 … 24/25; kontrola Σ vplyvov = ΔROE |
| 2.8 | **Altmanov model** | variant Z′ pre nekótované firmy: 0,717·X1 + 0,847·X2 + 3,107·X3 + 0,420·X4 + 0,998·X5. Družstvo nemá trhovú hodnotu, X4 = VK / CZ. Pásma: > 2,9 pevné zdravie; 1,23 – 2,9 šedá zóna; < 1,23 ohrozenie |
| 2.9 | **Quick test (Kralicek)** | 4 ukazovatele: VK/A, (CZ − fin. majetok)/CF, CF/T, EBIT/A → známky 1 – 5 → finančná stabilita, výnosová situácia, celková známka |
| 2.10 | Kontroly | Aktíva = Pasíva; Σ vplyvov = Δ; zhoda s FinStat |

**Metodické riziká, ktoré ošetríme:**
- Log. metóda zlyhá pri I_x = 1 (ln = 0) alebo pri zmene znamienka (strata ↔ zisk). Vtedy uvedieme poznámku a použijeme funkcionálnu metódu ako náhradu.
- Pri obrate T/A použijeme T = tržby z predaja tovaru (r. 03) + vlastných výrobkov (r. 04) + služieb (r. 05). Maloobchod má dominantné tržby za tovar. Pri ROS a dobách obratu použijeme rovnaké T.
- „ZETA model“ je proprietárna verzia Altmana. Na VŠB sa počíta Z-skóre (Z′), na čo v texte upozorníme.

---

## 3. Fáza – Výstupy (slovenčina)

| Súbor | Obsah | Publikum |
|---|---|---|
| `excel_vypocty_navod.md` | návod krok za krokom + vzorce Excel, mapovanie na riadky SK výkazov | tím |
| `report_coop_cadca.md` → PDF | min. 1500 slov / 5 – 6 strán A4; 6 kapitol (Úvod, Vývoj metrík, Pomerové ukazovatele, Rozklad ROE, Modely, Záver + SWOT + odporúčania) | vedenie a zamestnanci |
| `prezentacia_osnova.md` | osnova slide-by-slide, „slepé predstavenie“ firmy (hádanka → odhalenie), tím, výsledky, grafy, závery | študenti v cvičení |
| *(navyše podľa zadania)* `powerbi_navod.md` | štruktúra Power BI reportu: úvodná strana (tím + firma), stránky s tabuľkami/grafmi a krátkymi komentármi | študenti / LMS |

---

## 4. Harmonogram

| Kedy | Čo |
|---|---|
| teraz | dodáte výkazy + šablónu + odkaz |
| po dodaní | výpočty → `excel_vypocty_navod.md` (+ súhrnná tabuľka výsledkov na kontrolu) |
| následne | `report_coop_cadca.md` |
| následne | `prezentacia_osnova.md` (+ voliteľne Power BI návod) |
| 3 semináre | priebežne porovnať s tým, ako vyučujúci počíta v šablóne, a upraviť |
| do 19. 12. 2026 | odovzdanie do LMS (Excel, PDF report, PPT, Power BI) |
