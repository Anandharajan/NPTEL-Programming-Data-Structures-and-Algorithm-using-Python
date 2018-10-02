n=int(input())
a=list()
for i in range(n):
    k=int(input())
    a.append(k)
ans=list()
for k in range(n):
    ans.append(1)
for m in range(n-2,-1,-1):
    for p in range(m+1,n):
        if(a[p]%a[m]==0):
            if (1+ans[p] > ans[m]):
                ans[m]=1+ans[p]
print(max(ans))
