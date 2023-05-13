N = int(input())
A = list(map(int, input().split()))

ans=[]
for i in range(N-1):
    if A[i]<A[i+1]:
        ans.extend(range(A[i], A[i+1]))
    else:
        ans.extend(range(A[i], A[i+1], -1))
ans.append(A[N-1])
print(*ans)