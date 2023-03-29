N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# iマスまでの最大値
dp=[-151]*N
dp[0]=0
for i in range(N-1):
    dp[A[i]-1]=max(dp[A[i]-1], dp[i]+100)
    dp[B[i]-1]=max(dp[B[i]-1], dp[i]+150)
print(dp[N-1])