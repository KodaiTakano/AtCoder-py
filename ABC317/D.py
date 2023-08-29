N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

giseki_sum=0
for i in range(N):
    giseki_sum+=A[i][2]

B=A.copy()
giseki=0
for i in range(N):
    if A[i][0]>A[i][1]:
        giseki+=A[i][2]
        B.remove(A[i])

N=len(B)
A=B.copy()
for i in range(N):
    # 必要鞍替え人数
    A[i].append(A[i][1]-(A[i][0]+A[i][1])//2)
# A[i][3]:区獲得に必要な人数
A = sorted(A, reverse=False, key=lambda x: x[3])

# print(giseki_sum)
# print(giseki_sum-giseki)
# [print(*A[i]) for i in range(N)]

# dp[j]: j議席まで取るときの最小鞍替え人数
dp=[1000000000000]*(giseki_sum+1)
dp[0]=0

for i in range(N):
    for j in range(giseki_sum, A[i][2]-1, -1):
        dp[j]=min(dp[j], dp[j-A[i][2]]+A[i][3])

# print(dp)

need_giseki=giseki_sum//2-giseki

# print(need_giseki)

ans=1000000000000
for i in range(need_giseki+1, giseki_sum+1):
    ans=min(ans, dp[i])
print(ans)