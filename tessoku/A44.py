N, Q = map(int, input().split())

ans=list(range(1, N+1))
# print(ans)
rev=0
for i in range(Q):
    A = list(map(int, input().split()))
    if A[0]==1:
        if rev==0:
            ans[A[1]-1]=A[2]
        else:
            ans[N-A[1]]=A[2]
    if A[0]==2:
        if rev==0:
            rev=1
        else:
            rev=0
    if A[0]==3:
        if rev==0:
            print(ans[A[1]-1])
        else:
            print(ans[N-A[1]])