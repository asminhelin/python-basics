class Çalışan():
    def __init__(self,isim,maaş,departman):
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

    def zam_yap(self,zam_miktarı):
        self.maaş+=zam_miktarı

class Yönetici(Çalışan):
    def __init__(self,isim,maaş,departman,sorumlu_kişi_sayısı):
        super().__init__(isim,maaş,departman)
        self.sorumlu_kişi_sayısı=sorumlu_kişi_sayısı

    def bilgileri_göster(self):
        print("""
Yönetici Sınıfının Bilgileri
İsim:{}
Maaş:{}
Departman:{}
Sorumlu Kişi Sayısı:{}""".format(self.isim,self.maaş,self.departman,self.sorumlu_kişi_sayısı))

çalışan1=Çalışan("Ahmet Güçlü",70000,"Bilişim")
yönetici1=Yönetici("Ayşe Aslan",95000,"Bilişim",10)

çalışan1.bilgileri_göster()
yönetici1.bilgileri_göster()

print()

yönetici1.departman_değiştir("İnsan Kaynakları")
çalışan1.zam_yap(5000)

çalışan1.bilgileri_göster()
yönetici1.bilgileri_göster()

