a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

if (a==0):
    print("Bu ikinci dereceden bir denklem değildir.")
else:
    delta = b**2-(4*a*c)

    if (delta < 0):
        print("Denklemin gerçek kökü yoktur.")
    else:
        x1 = (-b-delta**0.5)/(2*a)
        x2 = (-b+delta**0.5)/(2*a)
        
        print("Birinci Kök= {}\nİkinci Kök= {}\n".format(x1,x2))