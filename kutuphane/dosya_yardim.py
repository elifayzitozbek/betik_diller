import json
from pathlib import Path
import pandas as pd

def csv_oku(yol: str):
    return pd.read_csv(yol)

def json_yaz(veri, dosya):
    Path(dosya).parent.mkdir(parents=True, exist_ok=True)
    with open(dosya, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=2)

def metin_yaz(icerik: str, dosya):
    Path(dosya).parent.mkdir(parents=True, exist_ok=True)
    with open(dosya, "w", encoding="utf-8") as f:
        f.write(icerik)
