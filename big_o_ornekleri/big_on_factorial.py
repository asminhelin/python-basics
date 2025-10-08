def nfactorial(n):
    if n==0:
        print("1")
        return
    else:
        for i in range(0,n):
            print(i)
            nfactorial(n-1) #recursive
nfactorial(2)