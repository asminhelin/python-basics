a=input("a:")
b=input("b:")

print("\nDeğiştirilmeden önceki değelerler:\na:{} b:{}".format(a,b))

a,b=b,a
print("\nDeğiştirildikten sonraki değelerler:\na:{} b:{}".format(a,b))