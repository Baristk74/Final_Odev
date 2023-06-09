from Calisan import Calisan
# Calisan modülünden Calisan sınıfını içe aktarıyoruz.


class BeyazYaka(Calisan):
    # Calisan sınıfının varisi olacak şekilde MaviYaka sınıfını oluşturuyoruz.
    def __init__(self, tc, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas, tesvik_primi):
        super().__init__(tc, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas)
        # Miras alınacak değerleri kullanabilmek için super metodunu kullanıyoruz.
        self.__tesvik_primi = tesvik_primi
        while self.__tesvik_primi < 100:
            self.__tesvik_primi = int(input("Lütfen 100'den büyük bir değer giriniz:"))
        # While ile girdinin istenmeyen bir girdi olmasını engelliyoruz.

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, yeni_tesvik_primi):
        while yeni_tesvik_primi < 100:
            yeni_tesvik_primi = int(input("Lütfen 100'den büyük bir değer giriniz:"))
        self.__tesvik_primi = yeni_tesvik_primi
# Private oluşturduğumuz tesvik_primi değişkeni için get-set metodu oluşturuyoruz.

    def zam_hakki(self):
        # Çalışanın tecrübe ve teşvik primi durumuna göre yeni maaş değerini hesaplıyoruz.
        if self.get_tecrube() / 12 < 2:
            zam_orani = self.get_tesvik_primi() * 10
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (zam_orani / 100))
        elif self.get_tecrube() / 12 >= 2 and self.get_tecrube() < 4 and self.get_maas() < 15000:
            zam_orani = (self.get_maas() % self.get_tecrube()) * 5 + self.get_tesvik_primi()
            self.set_yeni_maas(self.get_maas() + zam_orani)
        elif self.get_tecrube() / 12 >= 4 and self.get_maas() < 25000:
            zam_orani = (self.get_maas() % self.get_tecrube()) * 4 + self.get_tesvik_primi()
            self.set_yeni_maas(self.get_maas() + zam_orani)
        else:
            self.set_yeni_maas(self.get_maas())

    def __str__(self):
        self.zam_hakki()
        return f"Ad:{self.get_ad()}, Soyad:{self.get_soyad()}" \
               f" Tecrübe:{self.get_tecrube()} ay, Yeni Maaş:{self.get_yeni_maas()}"
# Değerleri string'e döndürmek için str metodunu kullanıyoruz.
