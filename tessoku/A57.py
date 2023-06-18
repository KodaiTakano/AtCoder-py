def base_n(num_10, n):
    if num_10==0:
        return 0
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return str_n[::-1]

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j]:穴jにいる時の2^i日後の場所
dp=[[0]*N for _  in range(30)]

for i in range(N):
    dp[0][i]=A[i]-1

for i in range(1, 30):
    for j in range(N):
        dp[i][j]=dp[i-1][dp[i-1][j]]
# [print(*dp[i]) for i in range(30)]

for _ in range(Q):
    X, Y = map(int, input().split())
    X-=1
    Y2=base_n(Y, 2)
    # print(Y2)
    YN=len(Y2)
    for i in range(YN):
        if Y2[i]=="1":
            X=dp[YN-i-1][X]
        # print(X)
    print(X+1)
    # break