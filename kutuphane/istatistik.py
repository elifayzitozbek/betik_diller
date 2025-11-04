def hesapla(df):
    return {
        "kayit_sayisi": int(len(df)),
        "ortalama_yas": float(df["age"].mean()) if len(df) else None,
        "sehir_sayim": df["city"].value_counts().sort_index().to_dict()
    }
