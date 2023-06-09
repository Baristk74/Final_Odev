class Insan:
    # Insan sınıfını oluşturuyoruz.
    def __init__(self, tc, ad, soyad, yas, cinsiyet, uyruk):
        self.__tc = tc
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk
# İhtiyaç duyulan özellikleri içeren init metodunu oluşturup, özelliklerimizi private olarak düzenliyoruz.

    def get_tc(self):
        return self.__tc

    def get_ad(self):
        return self.__ad

    def get_soyad(self):
        return self.__soyad

    def get_yas(self):
        return self.__yas

    def get_cinsiyet(self):
        return self.__cinsiyet

    def get_uyruk(self):
        return self.__uyruk

    def set_tc(self, tc):
        self.__tc = tc

    def set_ad(self, ad):
        self.__ad = ad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def set_yas(self, yas):
        self.__yas = yas

    def set_cinsiyet(self, cinsiyet):
        self.__cinsiyet = cinsiyet

    def set_uyruk(self, uyruk):
        self.__uyruk = uyruk
# Private değerlere ulaşabilmek ve değerleri düzenleyebilmek için get-set metodlarını oluşturuyoruz.

    def __str__(self):
        return f"Tc:{self.__tc}, Ad:{self.__ad}, Soyad:{self.__soyad}" \
               f" Yaş:{self.__yas}, Cinsiyet:{self.__cinsiyet}, Uyruk:{self.__uyruk}"
# Değerleri string'e döndürmek için str metodunu kullanıyoruz.
