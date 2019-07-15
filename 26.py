import math
x=int(input())
lis=list(map(int,input().split()))[:x]
lis.sort()
p=len(lis)
b=math.ceil(p/2)
print(b)
