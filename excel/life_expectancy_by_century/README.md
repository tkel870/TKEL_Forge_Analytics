# Life Expectancy by Century (Genealogical Analysis)

## Project Overview
This project analyzes lifespan trends across multiple centuries using genealogical data derived from my own ancestral records. The analysis focuses on understanding how age at death varies over time, while accounting for the limitations and inconsistencies common in historical records.

Rather than combining all data into a single dataset, each century was cleaned and analyzed independently using consistent validation rules. Summary statistics were then compiled to highlight long-term patterns while avoiding distortions caused by incomplete or unreliable records.

---

## Data Scope
- Time period analyzed: **13th through 20th centuries**
- Data source: Personal genealogical records
- Unit of analysis: Individual ancestors with sufficient birth and death information
- Analysis performed at the **century level** to respect historical context and data availability

---

## Data Cleaning & Validation
Historical genealogical data presents unique challenges, including partial dates, inconsistent formatting, and incomplete records. To ensure responsible analysis, the following rules were applied consistently across all centuries:

- Birth and death years were extracted from mixed-format date fields
- Original date text was preserved; no dates were imputed or guessed
- Records with non-date death values (e.g., “deceased”) were excluded from analysis
- Records with missing birth or death years were excluded from analysis
- Ages were calculated as `death year − birth year`
- Records with logically inconsistent dates (negative ages) were excluded
- Extreme outliers (ages greater than 110 years) were retained in the dataset but excluded from aggregate statistics
- An explicit `Include_in_analysis` flag was used to control which records contributed to summary metrics

These steps ensured that only valid, defensible records were used while maintaining transparency and auditability.

---

## Summary of Findings

### Per-Century Summary Statistics

| Century | Viable Records | Average Age | Median Age |
|-------|----------------|-------------|------------|
| 13th  | 256  | 57.84 | 59 |
| 14th  | 4,430 | 54.57 | 55 |
| 15th  | 7,344 | 56.07 | 56 |
| 16th  | 4,219 | 54.65 | 55 |
| 17th  | 1,808 | 53.75 | 58 |
| 18th  | 763  | 58.11 | 65 |
| 19th  | 248  | 60.33 | 67 |
| 20th  | 25   | 69.56 | 79 |

---

## Interpretation & Insights
- Average and median lifespans remain relatively stable across early centuries, reflecting adult survivorship rather than life expectancy at birth.
- Record counts peak in the 14th–16th centuries and decline sharply thereafter, indicating increasing documentation bias in later periods.
- Median age exceeds average age in later centuries, suggesting right-skewed distributions driven by a small number of long-lived individuals.
- Later-century results should be interpreted cautiously due to smaller sample sizes and selective record survival.
- Overall trends reflect improvements in longevity over time, while also highlighting the impact of data completeness and historical record-keeping practices.

---

## Tools Used
- Google Sheets
- Spreadsheet formulas (ARRAYFORMULA, COUNTIF, AVERAGEIF, FILTER)
- Data validation and rule-based inclusion logic

---

## Notes on Limitations
This analysis does not represent population-wide life expectancy. Results are influenced by survivorship bias, incomplete historical records, and the genealogical nature of the data. Findings are intended to illustrate trends within the available dataset rather than make broad demographic claims.

---

## Files in This Folder
- `life_expectancy_by_century.xlsx` — cleaned per-century datasets, summary statistics, and visualizations
