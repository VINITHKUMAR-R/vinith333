a=int(input())
sum=0
num=a
while num>0:
  digit=num%10
  sum=sum+digit**3
  num=num//10
if a==sum:
  print("yes")
else:
  print("no")
