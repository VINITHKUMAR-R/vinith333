x,y=input().split()
p=0
q=0
if len(x)>len(y):
  x,y=y,x
while q<len(x):
  p+=(ord(y[q])-ord(x[q]))
  q+=1
for q in range(q,len(y)):
  p+=ord(y[q])-ord('a')+1
print(p)
