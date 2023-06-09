from Insan import Insan
# Insan modülünden insan sınıfını içe aktarıyoruz.


class Issiz(Insan):
    # Insan sınıfının varisi olacak şekilde Issiz sınıfını oluşturuyoruz.
    def __init__(self, tc, ad, soyad, yas, cinsiyet, uyruk, mavi_yaka, beyaz_yaka, yonetici,  tecrube=None, statu=None):
        super().__init__(tc, ad, soyad, yas, cinsiyet, uyruk)
        # Miras alınacak değerleri kullanabilmek için super metodunu kullanıyoruz.
        self.__mavi_yaka = mavi_yaka
        self.__beyaz_yaka = beyaz_yaka
        self.__yonetici = yonetici
        if tecrube is None:
            tecrube = {"Mavi yaka": mavi_yaka, "Beyaz yaka": beyaz_yaka, "Yönetici": yonetici}
        # Girilen verileri tecrübe sözlüğüne atıyoruz.
        self.__tecrube = tecrube
        if statu is None:
            self.__statu = self.statu_bul()
        # statu_bul metoduyla statüyü bulup değişkenimize atıyoruz.
        # Issiz sınıfına ekleyeceğimiz özellikleri private olarak oluşturuyoruz.

    def get_mavi_yaka_tec(self):
        return self.__tecrube["Mavi yaka"]

    def get_beyaz_yaka_tec(self):
        return self.__tecrube["Beyaz yaka"]

    def get_yonetici_tec(self):
        return self.__tecrube["Yonetici"]

    def get_statu(self):
        return self.__statu

    def set_mavi_yaka_tec(self, yeni_mavi_yaka_tec):
        self.__mavi_yaka = yeni_mavi_yaka_tec

    def set_beyaz_yaka_tec(self, yeni_beyaz_yaka_tec):
        self.__beyaz_yaka = yeni_beyaz_yaka_tec

    def set_yonetici_tec(self, yeni_yonetici_tec):
        self.__yonetici = yeni_yonetici_tec
# Private değerlere ulaşabilmek ve değerleri düzenleyebilmek için get-set metodlarını oluşturuyoruz.

    def statu_bul(self):
        mavi_yaka_tec = self.__tecrube["Mavi yaka"]*0.2
        beyaz_yaka_tec = self.__tecrube["Beyaz yaka"]*0.35
        yonetici_tec = self.__tecrube["Yönetici"]*0.45
        if mavi_yaka_tec >= beyaz_yaka_tec and mavi_yaka_tec > yonetici_tec:
            return "Mavi yaka"
        elif beyaz_yaka_tec >= mavi_yaka_tec and beyaz_yaka_tec > yonetici_tec:
            return "Beyaz yaka"
        elif yonetici_tec >= beyaz_yaka_tec and yonetici_tec > mavi_yaka_tec:
            return "Yönetici"
# Tecrübe sözlüğündeki değerleri kullanarak uygun statüyü döndürmek için statu_bul metodunu oluşturuyoruz.

    def __str__(self):
        return f"Ad:{self.get_ad()}, Soyad:{self.get_soyad()}, Statü:{self.get_statu()}"
# Değerleri string'e döndürmek için str metodunu kullanıyoruz.
