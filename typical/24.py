N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0
for i in range(N):
    sum+=abs(A[i]-B[i])
if (K-sum)%2 == 0 and sum<=K:
    print("Yes")
else:
    print("No")