# Need to merge all the dataframs together and then do the preprocessing

import pandas as pd

def preprocess_data():
    # Load
    youth_unempl = pd.read_csv("data/raw/youth_unempl.csv")
    fed_funds = pd.read_csv("data/raw/fed_funds.csv")
    cpi = pd.read_csv("data/raw/cpi.csv")
    unrate = pd.read_csv("data/raw/unrate.csv")
    indpro = pd.read_csv("data/raw/indpro.csv")

    # Change (CPI, indpro) to growth rates
    cpi["value"] = cpi["value"].pct_change(12) * 100
    indpro["value"] = indpro["value"].pct_change(12) * 100

    # Column names
    youth_unempl = youth_unempl.rename(columns={"value": "youth_unempl"})
    fed_funds = fed_funds.rename(columns={"value": "fed_funds"})
    cpi = cpi.rename(columns={"value": "cpi"})
    unrate = unrate.rename(columns={"value": "unrate"})
    indpro = indpro.rename(columns={"value": "indpro"})

    # Merge
    df = youth_unempl.merge(fed_funds, on="date", how="left")
    df = df.merge(cpi, on="date", how="left")
    df = df.merge(unrate, on="date", how="left")
    df = df.merge(indpro, on="date", how="left")

    df["date"] = pd.to_datetime(df["date"])
    df["is_crisis"] = 0
    df.loc[(df["date"] >= "2008-09-01") & (df["date"] <= "2009-06-01"), "is_crisis"] = 1
    df.loc[(df["date"] >= "2020-03-01") & (df["date"] <= "2020-12-01"), "is_crisis"] = 1

    # Save original (before differencing) for EDA comparison
    df.dropna().to_csv("data/processed/merged_data.csv", index=False)

    # Take first difference to make the series stationary
    df["youth_unempl"] = df["youth_unempl"].diff()
    #df["unrate"] = df["unrate"].diff()

    # Drop rows with missing values
    df = df.dropna()

    # Save
    df.to_csv("data/processed/merged_data_diff.csv", index=False)
    print(f"Data processed: Columns: {len(df)}, {df['date'].min()} ~ {df['date'].max()}")

if __name__ == "__main__":
    preprocess_data()