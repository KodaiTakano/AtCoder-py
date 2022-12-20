import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

# count=0
# for i in range(N):
#     # print(bisect.bisect_right(A, A[i]+K)-i-1)
#     count+=(bisect.bisect_right(A, A[i]+K)-i-1)
# print(count)

B=[0]*(N-1)
for i in range(N-1):
    if i!=0:
        B[i]=B[i-1]

    while(B[i]<N-1 and A[B[i]+1]-A[i]<=K):
        B[i]+=1
#     print(B)

ans=0
for i in range(N-1):
    ans+=B[i]-i
print(ans)