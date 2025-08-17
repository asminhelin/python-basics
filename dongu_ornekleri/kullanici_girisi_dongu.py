print("""*********************
Kullanıcı Girişi
*********************
""")

sistem_kullanıcı_adı= "ali"

sistem_parola= "12345"
giriş_hakkı=3

while True:
    kullanıcı_adı= input("Kullanıcı Adı:")
    parola= input("Parola:")
    if (kullanıcı_adı==sistem_kullanıcı_adı and parola!=sistem_parola):
        print("Parola Hatalı.")
        giriş_hakkı-=1
    elif(kullanıcı_adı!=sistem_kullanıcı_adı and parola==sistem_parola):
       print("Kullanıcı Adı Hatalı")
       giriş_hakkı-=1
    elif(kullanıcı_adı!=sistem_kullanıcı_adı and parola!=sistem_parola):
        print("Kullanıcı Adı ve Parola Hatalı")
        giriş_hakkı-=1
    else:
        print("Sisteme Başarıyla Giriş Yapıldı.")
        break
    if (giriş_hakkı==0):
        print("Giriş Hakkınız Bitti.")
        break