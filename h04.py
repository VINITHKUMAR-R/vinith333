p=int(input())
r=list(map(int,input().split()))
for i in r:
  if r.count(i)==1:
    print(i)
