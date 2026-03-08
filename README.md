# U.S. Youth Unemployment Analysis (1991–2025)

> 🇰🇷 [한국어 버전 보기](README_KR.md)

---

## Motivation

Youth unemployment is a growing concern worldwide, accelerated by the rise of AI. As a 2nd-year mathematics student preparing for co-op in Canada — where only **15% of math students land their first co-op** without prior experience — this topic hits close to home.

This project analyzes U.S. youth unemployment data from 1991 to 2025, examining how each economic crisis impacted youth employment, how recovery speeds differed across crises, and what historical patterns tell us about the current and future outlook.

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
