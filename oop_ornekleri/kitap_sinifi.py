class Kitap():

    def __init__(self,isim,yazar,sayfa_sayısı,tür):
        self.isim=isim
        self.yazar=yazar
        self.sayfa_sayısı=sayfa_sayısı
        self.tür=tür

    def __str__(self):
        return "İsim:{}\nYazar:{}\nSayfa Sayısı:{}\nTürü:{}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)

    def __len__(self):
        return self.sayfa_sayısı

kitap1=Kitap("Dorian Gray'in Portresi","Oscar Wilde",258,"Gotik")
kitap2=Kitap("Bin Muhteşem Güneş","Khaled Hosseini",430,"Dram")

len(kitap1)

print(kitap1)
print()
print(kitap2)




