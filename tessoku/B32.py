N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))

# dp[i]:i個の時、先制が勝ちなら1、後手が勝ちなら0
dp=[0]*(N+1)

for i in range(N+1):
    if i<A[0]:
        continue
    for j in range(K):
        if i-A[j]>=0 and dp[i-A[j]]==0:
            dp[i]=1
# print(dp)
if dp[N]==1:
    print("First")
else:
    print("Second")