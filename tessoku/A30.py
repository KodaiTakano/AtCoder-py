# a%MOD*modinv(b)%MOD
def modinv(b, mod=10**9+7):
    return pow(b, mod-2, mod)

MOD = 1000000007

N, M = map(int, input().split())

n=1
for i in range(N):
    n*=(i+1)
    n%=MOD

r=1
for i in range(M):
    r*=(i+1)
    r%=MOD

nr=1
for i in range(N-M):
    nr*=(i+1)
    nr%=MOD

print(n%MOD*modinv(r*nr)%MOD)
