N, M = map(int, input().split())

MOD = 998244353
import math

# n,k,n-kが負になる可能性の時は例外処理を書く
def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))

if N==2:
    print(combinations_count(M, 2)%MOD)
if N==3:
    ans=1
    for _ in range(3):
        ans*=M
        ans%MOD
        M-=1
    print(ans%MOD)
if N>=4:
    ans=M
    for _ in range(N-2):
        ans*=(M-1)
        ans%=MOD
    print((ans*(M-1)%MOD+ans*(M-2)%MOD)%MOD)
