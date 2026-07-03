şekil=input("Hangi şeklin tipini öğrenmek istersiniz?:")

if (şekil=="Dörtgen"):

    print("Lütfen kenarları sırasıyla giriniz:")
    f=int(input("1.kenar:"))
    g=int(input("2.kenar:"))
    h=int(input("3.kenar:"))
    i=int(input("4.kenar:"))

    if (f==g==h==i):
        print("Dörtgen Tipi: Kare")
    elif (f==h and g==i):
        print("Dörtgen Tipi: Dikdörtgen")
    else:
        print("Dörtgen Tipi: Dörtgen")

elif (şekil=="Üçgen"):
    
    print("Lütfen kenarları sırasıyla giriniz:")
    f=int(input("1.kenar:"))
    g=int(input("2.kenar:"))
    h=int(input("3.kenar:"))

    if (abs(f+g)>h and abs(f+h)>g and abs(g+h)>f):
        if (f==g and f==h):
            print("Üçgen Tipi: Eşkenar Üçgen")
        elif ((f==g and f!=h) or (f==h and f!=g) or (g==h and g!=f)):
            print("Üçgen Tipi: İkizkenar Üçgen")
        else:
            print("Üçgen Tipi: Çeşitkenar Üçgen")
    else:
        print("Üçgen belirtmiyor...")
else:
    print("Geçersiz Şekil...")
    
