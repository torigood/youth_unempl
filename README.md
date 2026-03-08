# U.S. Youth Unemployment Analysis (1991–2025)

> 🇰🇷 [한국어 버전 보기](README_KR.md)

---

## Motivation

Youth unemployment is a growing concern worldwide, accelerated by the rise of AI. As a 2nd-year mathematics student preparing for co-op in Canada — where only **15% of math students land their first co-op** without prior experience — this topic hits close to home.

This project looks at U.S. youth unemployment from 1991 to 2025 from two angles:

1. **Descriptive analysis**: how each economic crisis hit youth employment differently, why recovery speeds varied, and what the historical pattern looks like leading into the AI era.
2. **Statistical modeling**: whether macro variables — interest rates, inflation, industrial output — actually move youth unemployment, or whether the series just follows the broader labor market.

---

## Key Findings

- Youth unemployment is a **lagging indicator** — it peaks ~2 years after the initial crisis shock
- **Structural crises** (2008) produce far slower recoveries than **external shocks** (COVID)
- Young workers are structurally last to be rehired in any recovery cycle
- AI-driven displacement may intensify this structural disadvantage going forward

---

## Dataset

| Variable | Source | Description |
|---|---|---|
| `youth_unempl` | FRED (SLUEM1524ZSUSA) | Youth unemployment rate, ages 15–24 |
| `fed_funds` | FRED (FEDFUNDS) | Federal funds effective rate |
| `cpi` | FRED (CPIAUCSL) | Consumer Price Index (YoY % change) |
| `unrate` | FRED (UNRATE) | Overall unemployment rate |
| `indpro` | FRED (INDPRO) | Industrial Production Index (MoM % change) |

**Period**: 1991-01 ~ 2025-12 (monthly)

---

## Youth Unemployment Rate Overview

![Youth Unemployment Rate 1991–2025](data/img/unempl_rate.png)

---

## Analysis

### 1991–2000: Long Boom and Declining Unemployment

Youth unemployment fell steadily from ~13.5% in 1991 to ~9.3% in 2000 — a near decade-long decline driven by three key factors:

- **Clinton-era fiscal policy** (1993–): Budget balancing and pro-growth policies improved the hiring environment.
- **Post-Cold War market expansion**: The collapse of the Soviet Union opened broader global markets for U.S. firms.
- **IT revolution**: The tech boom created an entirely new category of jobs, rapidly absorbing young workers.

However, the dot-com bubble began deflating in 2000, and the combined shock of the **2001 dot-com bust and 9/11** reversed the trend.

**References**
- [FactCheck.org — ~21 million jobs created under Clinton](https://www.factcheck.org/2007/12/clinton-and-economic-growth-in-the-90s/)
- [BLS Monthly Labor Review — Employment growth in the 1990s](https://www.bls.gov/opub/mlr/2000/12/art1full.pdf)

---

### 2000–2010: 9/11, Financial Crisis, and an All-Time Peak

The 9/11 attacks pushed youth unemployment from 10.49% (2001) to 12.36% (2003). Markets crashed and consumer confidence collapsed.

Recovery followed through 2007 (10.47%), but the **2008 Financial Crisis** — rooted in the 2007 housing bubble collapse — unleashed a wave of subprime mortgage defaults that rippled through the entire financial system.

Notably, unemployment **did not spike immediately in 2008**. Most firms held on initially, but as conditions deteriorated, mass layoffs followed with a ~2-year lag — peaking at an all-time high of **18.36% in 2010**. This is a textbook example of unemployment as a **lagging indicator**.

**References**
- [FRBSF — Economic impact of 9/11](https://www.frbsf.org/research-and-insights/publications/economic-letter/2001/12/the-us-economy-after-september-11/)
- [Federal Reserve History — The Great Recession and its aftermath](https://www.federalreservehistory.org/essays/great-recession-and-its-aftermath)

---

### 2010–2017: Obama Administration and the Slow Recovery

After peaking in 2010, youth unemployment took **~7 years** to fully recover. The Obama administration implemented healthcare reform, trade policy, and stimulus measures — household income rose and high school graduation rates improved.

![Recovery indicators under Obama](data/img/other_rate.png)

The slow pace reflects a structural reality: **young workers without experience are the last to be rehired** even as the broader economy recovers. Post-crisis, corporate hiring appetite was deeply suppressed.

**References**
- [BLS — Why employment recovery took 5+ years after the financial crisis](https://www.bls.gov/opub/mlr/2020/article/employment-recovery.htm)

---

### 2017–2025: COVID Shock, Fast Recovery, and the AI Era

Youth unemployment continued falling to **8.38% in 2019** — then COVID-19 drove it back up to **14.89% in 2020** as in-person service industries collapsed.

The recovery was strikingly different from 2008: rates fell to **9.7% in just one year** (2021). The rapid pivot to remote work and a surge in demand for tech workers enabled fast reabsorption of young workers. Where 2008 was a structural collapse, COVID was an **external shock with a temporary pause** — hence the dramatically faster recovery.

From 2023–2024, big tech layoffs pushed the rate slightly upward again as the pandemic-era hiring bubble deflated. As of 2025, the rate stands at **9.34%**, and AI-driven labor displacement adds further upward pressure.

> Anthropic's research report characterizes AI's impact on white-collar work as **"Great Depression-level"** for certain sectors. Elon Musk has predicted work will become optional within 10–20 years.

**References**
- [Pew Research Center — Post-COVID labor market recovery](https://www.pewresearch.org/politics/2025/02/12/how-covid-19-changed-u-s-workplaces/)
- [BLS — Long-term IT job outlook post-COVID](https://www.bls.gov/opub/btn/volume-11/mobile/what-the-long-term-impacts-of-the-covid-19-pandemic-could-mean-for-the-future-of-it-jobs.htm)
- [Fortune — Anthropic AI report: white-collar job losses](https://fortune.com/2026/03/06/ai-job-losses-report-anthropic-research-great-recession-for-white-collar-workers/)
- [Fortune — Elon Musk: work will be optional in 10–20 years](https://fortune.com/2026/01/19/when-does-elon-musk-say-work-will-be-optional-and-money-will-be-irrelevant-ai-robotics/)

---

## Modeling

See [`model.ipynb`](model.ipynb) for the full analysis.

### Why first-differenced data?
The raw series are non-stationary (unit roots), which breaks OLS assumptions. First-differencing makes the series stationary — so the model works with month-over-month changes rather than levels.

### Models

| Model | Description |
|---|---|
| OLS ADL (lag-2) | Autoregressive Distributed Lag — 2 AR lags on target, 1 lag on each macro variable, HC3 robust SEs |
| OLS ADL (lag-3) | Same as above but extended to 3 AR lags + 2nd lag on macro variables |
| ARIMAX | Grid-searched (p, q) by AIC; d=0 since data is already differenced |

An `is_crisis` dummy covers 2008 GFC and 2020 COVID — both are structural breaks that lag terms alone can't absorb.

### Results

All three models beat the naive "no change" baseline by ~7–9%:

| Model | RMSE | MAE |
|---|---|---|
| Naive (no change) | 0.9095 | 0.7532 |
| OLS (lag-2) | 0.8540 | 0.6847 |
| OLS (lag-3) | 0.8485 | 0.6878 |
| ARIMAX | 0.8421 | 0.6853 |

![OLS vs ARIMAX: Actual vs Predicted](data/img/ols_vs_arimax.png)

The three models perform nearly identically — the test period (2022–) covers a regime the model has never seen (post-COVID normalization + Fed rate hike cycle), which puts a ceiling on how well any of them can do.

### Key finding: coefficient analysis

Only `unrate` and `unrate_lag1` had statistically significant, practically meaningful coefficients:

1. **`unrate` coef ~1.8**: a 1pp rise in overall unemployment drives a ~1.8pp rise in youth unemployment. The shock is amplified — young workers absorb a disproportionate share of any labor market downturn.
2. **`fed_funds` and `cpi` insignificant**: rate hikes have no direct channel to youth unemployment. The Fed tightening cycle affects youth employment only indirectly, through the broader labor market.
3. **`unrate_lag1` negative**: an overshoot-correct pattern — the initial shock is larger than what actually sticks, and partially reverses the following month.

The main takeaway isn't that the model is weak — it's that **youth unemployment is structurally tied to the overall labor market, not an independent response to monetary or price variables**.

---

## Project Structure

```
macro_youth_unempl/
├── fetch_data.py          # Data collection via FRED API
├── preprocess.py          # Data cleaning and differencing
├── eda.ipynb              # Exploratory data analysis
├── model.ipynb            # Time series modeling (ADL)
├── data/
│   ├── raw/               # Raw FRED data
│   ├── processed/         # Merged & differenced datasets
│   └── img/               # Charts used in README
├── .env.example           # API key template
└── requriement.txt        # Python dependencies
```

---

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/torigood/youth_unempl.git
cd youth_unempl

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up API key
cp .env.example .env
# Edit .env and add your FRED API key (https://fred.stlouisfed.org/docs/api/api_key.html)

# 4. Fetch data
python fetch_data.py

# 5. Preprocess
python preprocess.py
```
