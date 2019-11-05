class Program():
    def __init__(self):
        self._veri = 0
    @property
    def veri(self):
        return self._veri
    @veri.setter
    def veri(self,yeni_değer):
        if yeni_değer % 2 == 0:
            self._veri = yeni_değer
        else:
            print("Sayı çift değil!")
        return self._veri
    @veri.deleter
    def veri(self):
        del self._veri

# self.veri'nin ismi önceden self.data'ydı. ve değiştirmek istedim. veri yaptım ama yine de data kelimesiyle de ulaşabilmesini
# istiyorum. o yüzden bu decorator'ı kullandım. ama şuan salt okunur. atama yapılabilmesini sağlamak için setter kullanmalıyım
# ismini değiştirince hala data kelimesiyle de ulaşabilmesini istememin bir sebebi şu ki: değiştirince kodun diğer kısımları mahvolacak
# ilgili özelliği o sırada çok zahir görsem bile mutlaka açıklama yaz, çünkü sonra unutuyosun