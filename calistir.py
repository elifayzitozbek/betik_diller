from kutuphane.dosya_yardim import csv_oku
from kutuphane.temizleyici import temizle
from kutuphane.istatistik import hesapla


def main():
    
    df = csv_oku("ornekler/kisiler.csv")

    
    temiz = temizle(df)

    
    ist = hesapla(temiz)

    
    
    print(" DÜZENLENMİŞ KAYITLAR")
   
    print(temiz.to_string(index=False))

   
    print(" İSTATİSTİKLER")
   
    print(f"Kayıt sayısı : {ist['kayit_sayisi']}")
    print(f"Ortalama yaş : {ist['ortalama_yas']}\n")

    print("Şehir dağılımı:")
    for sehir, adet in ist["sehir_sayim"].items():
        print(f" - {sehir}: {adet}")

    


if __name__ == "__main__":
    main()
