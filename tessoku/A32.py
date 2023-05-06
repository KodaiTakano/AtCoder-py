N, A, B = map(int, input().split())

# dp[i]:i個の時勝ちなら1負けなら0
dp=[0]*(N+1)
for i in range(N+1):
    if i<A:
        continue
    elif i-A>=0 and dp[i-A]==0:
        dp[i]=1
    elif i-B>=0 and dp[i-B]==0:
        dp[i]=1
if dp[N]==1:
    print("First")
else:
    print("Second")