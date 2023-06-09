from Calisan import Calisan
# Calisan modülünden Calisan sınıfını içe aktarıyoruz.


class MaviYaka(Calisan):
    # Calisan sınıfının varisi olacak şekilde MaviYaka sınıfını oluşturuyoruz.
    def __init__(self, tc, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas, yipranma_payi):
        super().__init__(tc, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas)
        # Miras alınacak değerleri kullanabilmek için super metodunu kullanıyoruz.
        self.__yipranma_payi = yipranma_payi
        while self.__yipranma_payi <= 0 or self.__yipranma_payi >= 1:
            self.__yipranma_payi = float(input("Lütfen 0,1 arasında bir değer giriniz:"))
        # While ile girdinin istenmeyen bir girdi olmasını engelliyoruz.

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yeni_yipranma_payi):
        if yeni_yipranma_payi <= 0 or yeni_yipranma_payi >= 1:
            yeni_yipranma_payi = float(input("Lütfen 0,1 arasında bir değer giriniz:"))
        self.__yipranma_payi = yeni_yipranma_payi
# Private oluşturduğumuz yipranma_payi değişkeni için get-set metodu oluşturuyoruz.

    def zam_hakki(self):
        # Çalışanın tecrübe ve yıpranma payı durumuna göre yeni maaş değerini hesaplıyoruz.
        if self.get_tecrube() / 12 < 2:
            zam_orani = self.__yipranma_payi * 10
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (zam_orani / 100))

        elif self.get_tecrube() / 12 >= 2 and self.get_tecrube() < 4 and self.get_maas() < 15000:
            zam_orani = (self.get_maas() % self.get_tecrube()) / 2 + (self.__yipranma_payi * 10)
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (zam_orani / 100))

        elif self.get_tecrube() / 12 >= 4 and self.get_maas() < 25000:
            zam_orani = (self.get_maas() % self.get_tecrube()) / 3 + (self.__yipranma_payi * 10)
            self.set_yeni_maas(self.get_maas() + self.get_maas() * (zam_orani / 100))

        else:
            self.set_yeni_maas(self.get_maas())

    def __str__(self):
        self.zam_hakki()
        return f"Ad:{self.get_ad()}, Soyad:{self.get_soyad()}" \
               f" Tecrübe:{self.get_tecrube()} ay, Yeni Maaş:{self.get_yeni_maas()}"
# Değerleri string'e döndürmek için str metodunu kullanıyoruz.
