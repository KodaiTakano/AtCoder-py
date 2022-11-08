N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

count=1
ans=[0]*N
index=0
for i in range(N-1):
    if(A[i]==A[i+1]):
        count+=1
    else:
        ans[index]=count
        count=1
        index+=1
ans[index]=count
print(*ans)