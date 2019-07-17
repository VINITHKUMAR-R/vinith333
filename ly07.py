p=list(input())
q=len(p)
for i in range(0,q,2):
  p[i],p[i+1]=p[i+1],p[i]
print(*p,sep="")
