x=int(input())
i=1
fv=0
sv=1
while i<x+1:
  if (i<=1):
    value=i
  else:
    value=fv+sv
    fv=sv
    sv=value
 print(value,end=" ")
 i=i+1
