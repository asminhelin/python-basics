şekil=input("Hangi şeklin tipini öğrenmek istersiniz?:")

if (şekil=="Dörtgen"):

    print("Lütfen kenarları sırasıyla giriniz:")
    a=int(input("1.kenar:"))
    b=int(input("2.kenar:"))
    c=int(input("3.kenar:"))
    d=int(input("4.kenar:"))

    if (a==b==c==d):
        print("Dörtgen Tipi: Kare")
    elif (a==c and b==d):
        print("Dörtgen Tipi: Dikdörtgen")
    else:
        print("Dörtgen Tipi: Dörtgen")

elif (şekil=="Üçgen"):
    
    print("Lütfen kenarları sırasıyla giriniz:")
    a=int(input("1.kenar:"))
    b=int(input("2.kenar:"))
    c=int(input("3.kenar:"))

    if (abs(a+b)>c and abs(a+c)>b and abs(b+c)>a):
        if (a==b and a==c):
            print("Üçgen Tipi: Eşkenar Üçgen")
        elif ((a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)):
            print("Üçgen Tipi: İkizkenar Üçgen")
        else:
            print("Üçgen Tipi: Çeşitkenar Üçgen")
    else:
        print("Üçgen belirtmiyor...")
else:
    print("Geçersiz Şekil...")
