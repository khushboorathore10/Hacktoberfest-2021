#copyright prashant-2906
n=input().split()
ans=[]
a=0
for i in n:
  a+=int(i)
  ans.append(a)
print(*ans,end="")
