a=int(input())
lis=list(map(int,input().split()))[:a]
lis.sort()
print(*lis,end="")
