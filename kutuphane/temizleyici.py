import pandas as pd
from kutuphane.kontrol import zorunlu_alanlar  

GEREKEN = ["name", "age", "city"]

@zorunlu_alanlar(GEREKEN)
def temizle(df):
    df = df.copy()
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df = df.dropna(subset=["age"])
    for alan in ["name", "city"]:
        df[alan] = (
            df[alan].astype(str)
            .str.strip()
            .str.strip('"')
            .str.strip("'")
        )
    df["age"] = df["age"].astype(int)
    df = df[df["name"].str.len() > 0]
    return df.reset_index(drop=True)
