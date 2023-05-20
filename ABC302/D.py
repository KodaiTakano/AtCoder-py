import bisect

N, M, D = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
# print(A)
# print(B)

ans=-1
for i in range(N):
    # print(i)
    # print(A[i]-D)
    # print(bisect.bisect_right(B, A[i]-D))
    # print(A[i]+D)
    # print(bisect.bisect_left(B, A[i]+D))
    # print()
    
    j=bisect.bisect_right(B, A[i]-D)
    if 0<=j and j<=M-1:
        if A[i]>=B[j] and A[i]-B[j]<=D and ans<A[i]+B[j]:
            ans=A[i]+B[j]

    j=bisect.bisect_left(B, A[i]+D)
    if 0<=j and j<=M-1:
        if A[i]<=B[j] and B[j]-A[i]<=D and ans<A[i]+B[j]:
            ans=A[i]+B[j]
 
    j=bisect.bisect_left(B, A[i]-D)
    if 0<=j and j<=M-1:
        if A[i]>=B[j] and A[i]-B[j]<=D and ans<A[i]+B[j]:
            ans=A[i]+B[j]
    
    j=bisect.bisect_right(B, A[i]+D)
    if 0<=j and j<=M-1:
        if A[i]<=B[j] and B[j]-A[i]<=D and ans<A[i]+B[j]:
            ans=A[i]+B[j]

print(ans)
    