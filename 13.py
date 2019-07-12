r=int(input())
for i in range(2,r):
  if(r%i==0):
    print("no")
    break
else:
  print("yes")
