from Insan import Insan
# Insan modülünden Insan sınıfını içe aktarıyoruz.


class Calisan(Insan):
    # Insan sınıfının varisi olacak şekilde Calisan sınıfını oluşturuyoruz.
    def __init__(self, tc, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas=None):
        super().__init__(tc, ad, soyad, yas, cinsiyet, uyruk)
        # Miras alınacak değerleri kullanabilmek için super metodunu kullanıyoruz.
        self.__sektor = sektor
        while self.__sektor not in ["Teknoloji", "Muhasebe", "İnşaat", "Diğer"]:
            self.__sektor = input("Lütfen Teknoloji, Muhasebe, İnşaat ya da Diğer seçeneklerinden birini giriniz:")
        # While ile girdinin istenmeyen bir girdi olmasını engelliyoruz.
        self.__tecrube = tecrube
        self.__maas = maas
        if yeni_maas is None:
            self.__yeni_maas = yeni_maas

    def get_sektor(self):
        return self.__sektor

    def get_tecrube(self):
        return self.__tecrube

    def get_maas(self):
        return self.__maas

    def get_yeni_maas(self):
        return self.__yeni_maas

    def set_sektor(self, girilen_sektor):
        while girilen_sektor not in ["Teknoloji", "Muhasebe", "İnşaat", "Diğer"]:
            girilen_sektor = input("Lütfen Teknoloji, Muhasebe, İnşaat ya da Diğer seçeneklerinden birini giriniz:")
        self.__sektor = girilen_sektor

    def set_tecrube(self, yeni_tecrube):
        self.__tecrube = yeni_tecrube

    def set_maas(self, yeni_maas):
        self.__maas = yeni_maas

    def set_yeni_maas(self, yeni_yeni_maas):
        self.__yeni_maas = yeni_yeni_maas
# Private değerlere ulaşabilmek ve değerleri düzenleyebilmek için get-set metodlarını oluşturuyoruz.

    def zam_hakki(self):
        # Çalışanın tecrübe ve güncel maaş durumuna göre yeni maaş değerini hesaplıyoruz.
        if self.__tecrube / 12 < 2:
            zam_orani = 0
            self.__yeni_maas = self.__maas + self.__maas * (zam_orani / 100)
        elif self.__tecrube / 12 >= 2 and self.__tecrube < 4 and self.__maas < 15000:
            zam_orani = self.__maas % self.__tecrube
            self.__yeni_maas = self.__maas + self.__maas * (zam_orani / 100)
        elif self.__tecrube / 12 >= 4 and self.__maas < 25000:
            zam_orani = (self.__maas % self.__tecrube) / 2
            self.__yeni_maas = self.__maas + self.__maas * (zam_orani / 100)
        else:
            self.__yeni_maas = self.__maas

    def __str__(self):
        self.zam_hakki()
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}" \
               f" Tecrübe: {self.get_tecrube()} ay, Yeni Maaş: {self.get_yeni_maas()}"
# Değerleri string'e döndürmek için str metodunu kullanıyoruz.
