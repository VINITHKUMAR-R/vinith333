p=int(input())
q=list(map(int,input().split()))[:p]
for i in range(len(q)):
      if((i%2==0)and(q[i]%2!=0)or(i%2!=0)and(q[i]%2==0)):
           print(q[i],end=" ")
