import sys
p=int(input())
q=list(map(int,input().split()))
for i in q:
    if(q.count(i)>1):
        print(i)
        sys.exit()
print("unique")
