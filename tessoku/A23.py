def base_n(num_10, n):
    if num_10==0:
        return 0
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

# dp[i][S] iまでのクーポン券からいくつか使うとS内の集合が無料で買える。この時の選んだ最小枚数。
# Sは2進数→10に直す

dp=[[1000000000]*(1<<N) for _ in range(M+1)]
dp[0][0]=0

for i in range(1, M+1):
    for S in range(1<<N):
        # クーポンを使わない場合
        dp[i][S]=min(dp[i-1][S],dp[i][S])
        
        # already:すでに無料になっている商品
        already=set()

        TWO=list(str(base_n(S,2)))
        TWO.reverse()
        # if i==1:
        #     print(list(TWO))
        for j in range(len(TWO)):
            if TWO[j]=='1':
                already.add(j)

        # if i==1:
        #     print(already)
        
        # クーポンでタダになる商品(空配列=タダのものなし,0スタート)
        for j in range(N):
            if A[i-1][j]==1:
                already.add(j)
        nxt_S=0
        for n in already:
            nxt_S+=1<<n
        # print(nxt_S)
        # クーポンを使う場合
        dp[i][nxt_S]=min(dp[i-1][S]+1, dp[i][nxt_S])

if dp[M][(1<<N)-1]==1000000000:
    print(-1)
else:
    print(dp[M][(1<<N)-1])

# [print(*dp[i]) for i in range(M+1)]