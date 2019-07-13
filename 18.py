p,q=map(int,input().split())
for i in range(p+1,q):
  sum=0
  temp=i
  while(temp>0):
    r=temp%10
    sum=sum+r**3
    temp=temp//10
  if(i==sum):
    print(i,end=" ")
