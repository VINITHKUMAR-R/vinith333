a,b=map(int,input().split())
count=0
for i in range(a,b+1):
    if i>1:
        for n in range(2,i):
            if(i%n==0):
                break
        else:
            count=count+1
print(count)
