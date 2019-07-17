p=int(input())
q=[int(i) for i in input().split()]
a=[]
for i in range(0,len(q)):
  if i==q[i]:
    a.append(q[i])
if len(a)==0:
  print("-1")
else:
  for x in range(len(a)):
     print(a[x],end=" ")
