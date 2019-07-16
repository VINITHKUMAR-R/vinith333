x=int(input())
y=list(map(int,input().split()))[:x]
py=[]
for i in y:
  if y.count(i)>1:
    if str(i) not in py:
      py.append(str(i))
if len(py)==0:
    print("unique")
else:
    py.sort()
    print(" ".join(py))
  
