p=list(input())
q=" "
for i in range(len(p)):
  if q in p:
    p.remove(q)
print(len(p))
