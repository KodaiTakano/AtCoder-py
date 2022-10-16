N, K = map(int, input().split())

MOD = 1000000007

if N==1:
    print(K)
if N==2:
    print(K*(K-1)%MOD)
if N==3:
    print(K*(K-1)%MOD*(K-2)%MOD)
if N>=4:
    print(pow(K-2, N-3, MOD)*K%MOD*(K-1)%MOD*(K-2)%MOD)
