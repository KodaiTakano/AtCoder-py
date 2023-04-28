import bisect

N = int(input())
size=[]
for _ in range(N):
    x, y = map(int, input().split())
    size.append([x,y])
# print(size)

size = sorted(size, reverse=True, key=lambda x: (x[1])) #1列目を基準にして降順ソート
size = sorted(size, reverse=False, key=lambda x: (x[0])) #0列目を基準にして昇順ソート
# print(size)

# dp[i]: 最後の箱がsize[i]である入れ方のうち最大の重ね数
dp=[0]*N
dp[0]=1

# 計算時間(N^2)
# for i in range(1, N):
#     for j in range(0, i):
#         if size[i][0]!=size[j][0] and size[i][1]>size[j][1]:
#             dp[i]=max(dp[i], dp[j]+1)


# L[x]: 重ね数xの最後の要素として考えられる最小値
#       dp[k]=xを満たすようなkにおけるsize[i]の最小値
L=[1000000]*(N+1)
L[0]=0
L[1]=size[0][1]
ans=1
for i in range(1, N):
    pos=bisect.bisect_left(L, size[i][1])
    dp[i]=max(dp[i],pos)

    L[dp[i]]=size[i][1]
    if ans<dp[i]:
        ans=dp[i]
# print(dp)
print(ans)