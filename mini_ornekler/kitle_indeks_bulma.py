print("Vücut Kitle İndeksi Hesaplama\n")

boy=float(input("Boy:"))
kilo=float(input("Kilo:"))
vki=float(kilo/(boy**2))

print("Vücut Kitle İndeksi:",vki)

if (vki<18.5):
    print("Zayıf")
elif (vki>=18.5 and vki<25):
    print("Normal")
elif (vki>=25 and vki<30):
    print("Fazla Kilolu")
else:
    print("Obez")