x=input()
y=list(map(str,input().split()))
y.sort(reverse=True)
z=list(map(int,y))
if sum(z)==0:
    print("0")
else:
    a="".join(y)
    print(a)
