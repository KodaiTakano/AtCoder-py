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

N, K = map(int, input().split())

# dp[i][j]:数jの2^i回後の数値
dp=[[0]*(N+1) for _  in range(30)]

# sum(list(map(int, str(n)))):nの各位の和
for j in range(N+1):
    dp[0][j]=j-sum(list(map(int, str(j))))

# [print(*dp[i]) for i in range(5)]

for i in range(1, 30):
    for j in range(N+1):
        dp[i][j]=dp[i-1][dp[i-1][j]]

# [print(*dp[i]) for i in range(5)]

K2=base_n(K, 2)
KN=len(K2)
for i in range(N):
    ans=i+1
    for j in range(KN):
        if K2[j]=="1":
            ans=dp[KN-j-1][ans]
    print(ans)