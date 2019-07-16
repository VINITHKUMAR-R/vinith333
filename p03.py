x,y=input().split()
p=len(x) if len(x)<len(y) else len(y)
q=abs(len(y)-len(x))
count=q
for i in range(p):
  if(x[i]!=y[i]):
    count+=1
print(count)
