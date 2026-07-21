class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim=isim
        self.maaş=maaş
        self.departman=departman

    def bilgileri_göster(self):
        print("""
Çalışan Sınıfının Bilgileri
İsim:{}
Maaş:{}
Departman:{}""".format(self.isim,self.maaş,self.departman))
        
    def departman_değiştir(self,yeni_departman):
        self.departman=yeni_departman

class Yönetici(Çalışan):
    pass

yönetici1=Yönetici("Ayşe Aslan",95000,"Bilişim")
yönetici1.bilgileri_göster()

print()

yönetici1.departman_değiştir("İnsan Kaynakları")
yönetici1.bilgileri_göster()