class Yazılımcı():
    def __init__(self,ad,soyad,numara,maaş,diller):
        self.ad=ad
        self.soyad=soyad
        self.numara=numara
        self.maaş=maaş
        self.diller=diller

    def bilgiler(self):
        print("""
Yazılımcı Objesinin Özellikleri
Ad:{}
Soyad:{}
Numara:{}
Maaş:{}
Diller:{}""".format(self.ad,self.soyad,self.numara,self.maaş,self.diller))

    def zam_yap(self,zam_miktarı):
        print("Zam yapılıyor...")
        self.maaş+=zam_miktarı

    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor...")
        self.diller.append(yeni_dil)

yazılımcı1=Yazılımcı("Ali","Kaya",123456,80000,["Python","Java"])
        
yazılımcı1.bilgiler()

print()
yazılımcı1.dil_ekle("C")
yazılımcı1.zam_yap(5000)

yazılımcı1.bilgiler()