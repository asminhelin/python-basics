import math
def logn(n):
    while n>1:
        n=math.floor(n/2)
        print(n)
logn(32)