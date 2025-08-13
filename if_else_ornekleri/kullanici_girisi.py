print("""*********************
Kullanıcı Girişi
*********************
""")

sistem_kullanıcı_adı= "ali"
sistem_parola= "12345"

kullanıcı_adı= input("Kullanıcı Adı:")
parola= input("Parola:")

if (kullanıcı_adı==sistem_kullanıcı_adı and parola!=sistem_parola):
    print("Parola Hatalı.")
elif(kullanıcı_adı!=sistem_kullanıcı_adı and parola==sistem_parola):
    print("Kullanıcı Adı Hatalı")
elif(kullanıcı_adı!=sistem_kullanıcı_adı and parola!=sistem_parola):
    print("Kullanıcı Adı ve Parola Hatalı")
else:
    print("Sisteme Başarıyla Giriş Yapıldı.")