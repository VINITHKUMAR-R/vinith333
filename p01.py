def lof(p):
    count=""
    for i in range(min([len(x) for x in p])):
        current=p[0][i]
        for j in range(1,n):
            if not(current==p[j][i]):
                return count
        count+=current
    return count
    
n=int(input())
lis=[]
for i in range(n):
    lis.append(input())
print(lof(lis))
