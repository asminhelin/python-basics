a=input("a:")
b=input("b:")

print("\nDeğiştirilmeden Önceki Değelerler:\na:{} b:{}".format(a,b))

a,b=b,a
print("\nDeğiştirildikten Sonraki Değelerler:\na:{} b:{}".format(a,b))