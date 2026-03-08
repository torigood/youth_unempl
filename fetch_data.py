import os
from fredapi import Fred
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
fred = Fred(api_key=os.getenv("FRED_API_KEY"))

SERIES = {
    "LNS14000012":     "youth_unempl",
    #"A191RL1Q225SBEA": "gdp_growth",
    "FEDFUNDS":        "fed_funds",
    "CPIAUCSL":        "cpi",
    "UNRATE":          "unrate",
    "INDPRO":           "indpro",
}

for code, name in SERIES.items():
    df = fred.get_series(code, observation_start="1990-01-01").reset_index()
    df.columns = ["date", "value"]
    df.to_csv(f"data/raw/{name}.csv", index=False)