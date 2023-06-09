import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from Mavi_yaka import MaviYaka
from Beyaz_yaka import BeyazYaka
# pandas modülünü pd olarak içe aktarıyoruz.
# Insan modülünden Insan sınıfını içe aktarıyoruz.
# Issiz modülünden Issiz sınıfını içe aktarıyoruz.
# Calisan modülünden Calisan sınıfını içe aktarıyoruz.
# Mavi_yaka modülünden MaviYaka sınıfını içe aktarıyoruz.
# Beyaz_yaka modülünden BeyazYaka sınıfını içe aktarıyoruz.


pd.set_option("display.max_columns", 15)
# Görüntülenecek sütun sayısını 15 yapıyoruz.
kisi1 = Insan(tc=218223, ad="Yağmur", soyad="Karahanlı", yas=20, cinsiyet="Kadın", uyruk="Türk")
kisi2 = Insan(tc=218224, ad="Barış", soyad="Tunçkanat", yas=20, cinsiyet="Erkek", uyruk="Türk")
# Insan sınıfına örnek kişiler giriyoruz.
kisi3 = Issiz(tc=218225, ad="Selcan", soyad="Kırayıt", yas=20, cinsiyet="Kadın", uyruk="Slav",
              mavi_yaka=9, beyaz_yaka=12, yonetici=6)
kisi4 = Issiz(tc=218226, ad="Ali", soyad="Kerpeten", yas=42, cinsiyet="Erkek", uyruk="Türk",
              mavi_yaka=4, beyaz_yaka=6, yonetici=12)
kisi5 = Issiz(tc=218227, ad="Melih", soyad="Tatlısu", yas=22, cinsiyet="Erkek", uyruk="Slav",
              mavi_yaka=12, beyaz_yaka=6, yonetici=2)
# Issiz sınıfına örnek kişiler giriyoruz.
kisi6 = Calisan(tc=218228, ad="Baran", soyad="Yıldırım", yas=25, cinsiyet="Erkek", uyruk="Kürt",
                sektor="Diğer", tecrube=60, maas=12000, yeni_maas=0)
kisi7 = Calisan(tc=218229, ad="Bekir", soyad="Karaca", yas=27, cinsiyet="Erkek", uyruk="Laz",
                sektor="Teknoloji", tecrube=123, maas=28000, yeni_maas=0)
kisi8 = Calisan(tc=218230, ad="Mukaddes", soyad="Şekercizade", yas=48, cinsiyet="Kadın", uyruk="Arap",
                sektor="Diğer", tecrube=172, maas=35650, yeni_maas=0)
# Calisan sınına örnek kişiler giriyoruz.
kisi9 = MaviYaka(tc=218231, ad="Kenan", soyad="Kırayıt", yas=62, cinsiyet="Erkek", uyruk="Türk",
                 sektor="Muhasebe", tecrube=300, maas=32300, yeni_maas=0, yipranma_payi=0.2)
kisi10 = MaviYaka(tc=218232, ad="Polat", soyad="Alemdar", yas=44, cinsiyet="Erkek", uyruk="Türk",
                  sektor="İnşaat", tecrube=999, maas=99999, yeni_maas=0, yipranma_payi=0.9)
kisi11 = MaviYaka(tc=218233, ad="Hürrem", soyad="Şehzadedoğuran", yas=70, cinsiyet="Kadın", uyruk="Slav",
                  sektor="Teknoloji", tecrube=360, maas=90000, yeni_maas=0, yipranma_payi=0.7)
# MaviYaka sınıfına örnek kişiler giriyoruz.
kisi12 = BeyazYaka(tc=218234, ad="Bihter", soyad="Memnu", yas=28, cinsiyet="Kadın", uyruk="Çerkez",
                   sektor="Diğer", tecrube=6, maas=39708, yeni_maas=0, tesvik_primi=221)
kisi13 = BeyazYaka(tc=218235, ad="Ezel", soyad="Bayraktar", yas=32, cinsiyet="Erkek", uyruk="Türk",
                   sektor="Muhasebe", tecrube=148, maas=43364, yeni_maas=0, tesvik_primi=124)
kisi14 = BeyazYaka(tc=218236, ad="Adnan", soyad="Kazıkyiyengiloğlu", yas=55, cinsiyet="Erkek", uyruk="Türk",
                   sektor="İnşaat", tecrube=324, maas=13800, yeni_maas=0, tesvik_primi=108)
# BeyazYaka sınıfına örnek kişiler giriyoruz.
print("Örnek insanlar:\n", kisi1.__str__(), "\n", kisi2.__str__(), "\n")
print("Örnek işsizler:\n", kisi3.__str__(), "\n", kisi4.__str__(), "\n", kisi5.__str__(), "\n")
print("Örnek çalışanlar:\n", kisi6.__str__(), "\n", kisi7.__str__(), "\n", kisi8.__str__(), "\n")
print("Örnek mavi yakalar\n", kisi9.__str__(), "\n", kisi10.__str__(), "\n", kisi11.__str__(), "\n")
print("Örnek beyaz yakalar:\n", kisi12.__str__(), "\n", kisi13.__str__(), "\n", kisi14.__str__(), "\n")
# Oluşturduğumuz örnekleri kisileri str metodu ile ekrana yazdırıyoruz.
kisiler = [kisi6, kisi7, kisi8, kisi9, kisi10, kisi11, kisi12, kisi13, kisi14]
# DataFrame'de kullanacağımız kisileri listeliyoruz.
sozlukler = {"Tc": [], "Ad": [], "Soyad": [], "Yaş": [], "Cinsiyet": [], "Uyruk": [], "Sektör": [], "Tecrübe": [],
            "Maaş": [], "Yeni Maaş": [], "Yıpranma Payı": [], "Teşvik Primi": [], "Çalışan Tipi": []}
# DataFrame oluşturabilmek için her özellik için sözlük oluşturuyoruz.
for kisi in kisiler:
    kisi.zam_hakki()
    sozlukler["Tc"].append(kisi.get_tc())
    sozlukler["Ad"].append(kisi.get_ad())
    sozlukler["Soyad"].append(kisi.get_soyad())
    sozlukler["Yaş"].append(kisi.get_yas())
    sozlukler["Cinsiyet"].append(kisi.get_cinsiyet())
    sozlukler["Uyruk"].append(kisi.get_uyruk())
    sozlukler["Sektör"].append(kisi.get_sektor())
    sozlukler["Tecrübe"].append(kisi.get_tecrube())
    sozlukler["Maaş"].append(kisi.get_maas())
    sozlukler["Yeni Maaş"].append(kisi.get_yeni_maas())
    sozlukler["Çalışan Tipi"].append(type(kisi).__name__)
    # Her kisi'nin özelliklerini, o özellik için oluşturulmuş sözlüklere ekliyoruz.
    try:
        sozlukler["Yıpranma Payı"].append(kisi.get_yipranma_payi())
    except AttributeError:
        sozlukler["Yıpranma Payı"].append(None)
    try:
        sozlukler["Teşvik Primi"].append(kisi.get_tesvik_primi())
    except AttributeError:
        sozlukler["Teşvik Primi"].append(None)
# Değeri olmayan özellikler sebebiyle hata almamak için, o özelliklere "None" değeri atıyoruz.
# Örnek a:
df = pd.DataFrame(sozlukler).fillna(0)
# Boş olan değerlere 0 atıyoruz.

# Örnek b:
grup_df = df.groupby("Çalışan Tipi").agg({"Yeni Maaş": "mean", "Tecrübe": "mean"})
print("\nÇalışan tiplerine göre yeni maaş, tecrübe ortalamaları:\n", grup_df)
# Kişileri Çalışan tipine göre gruplandırıp; yeni maaş ve tecrübe bilgilerinin ortalamalarını ekrana yazdırıyoruz.

# Örnek c:
print("\nMaaşı 15000 TL üzerinde olanların sayısı:", len(df[df["Maaş"] > 15000]))
# Maaş değeri 15000 üzerinde olanlar için df oluşturup uzunluk değerinden kişi sayısını elde ediyoruz.
# Örnek d:
print("\nYeni maaş değerine göre sıralama:\n", df.sort_values("Yeni Maaş"))
# Elimizdeki df'den "Yeni Maaş" değerine göre sıralıyoruz.

# Örnek e:
print("3 Yıldan fazla tecrübesi olan Beyaz yaka:", df.loc[(df["Çalışan Tipi"] == "BeyazYaka") & (df["Tecrübe"] >= 36)])
# BeyazYaka ve 36 aydan çok tecrübesi olan kişileri ekrana yazdırıyoruz.

# Örnek f:
print("\nYeni maaşı 10000 TL üzerinde olanlardan, 2-5 arasında olanların tc ve yeni maaş sütunlarını gösterme:")
print(df.loc[(df["Yeni Maaş"] > 10000) & (df.index > 2) & (df.index < 5), ["Tc", "Yeni Maaş"]])
# "Yeni Maaş" sütununa özel bir sıralama oluşturup istenilen aralıktaki kisiler için
# sadece "Tc, Yeni Maaş" sütunlarıyla ekrana yazdırıyoruz.

# Örnek g:
print("\nKırpılmış Şablon:\n", df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]])
# İstenilen sütunları için şablonu tekrar yazdırıyoruz.
