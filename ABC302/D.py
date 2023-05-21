import bisect

N, M, D = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
# print(A)
# print(B)

ans=-1
for i in range(N):
    # print(bisect.bisect_left(B, A[i]+D))
    
    j=bisect.bisect_left(B, A[i]+D)
    # print(j)
    if 0<=j and j<=M-1:
        if B[j]<=A[i]+D:
            ans=max(ans, A[i]+B[j])
    j-=1
    if 0<=j and j<=M-1:
        if A[i]-D<=B[j] and B[j]<=A[i]+D:
            ans=max(ans, A[i]+B[j])

print(ans)
    