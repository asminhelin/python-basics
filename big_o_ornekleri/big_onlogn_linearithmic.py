import math
def nlogn(n):
    lim=n
    while n>1:
        n=math.floor(n/2)
        for i in range(1,lim):
            print(i)
nlogn(8)