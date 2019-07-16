pa=input()
a=b=c=0
for i in range(len(pa)):
  if pa[i].isalpha():
    a+=1
  elif pa[i].isnumeric():
    b+=1
  else:
    c+=1
print(c)

