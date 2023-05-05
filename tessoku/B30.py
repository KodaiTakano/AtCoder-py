H, W = map(int, input().split())

# H+W-2の中からH-1個選ぶ

# a%MOD*modinv(b)%MOD
def modinv(b, mod=10**9+7):
    return pow(b, mod-2, mod)

MOD = 1000000007

n=1
for i in range(H+W-2):
    n*=(i+1)
    n%=MOD

r=1
for i in range(H-1):
    r*=(i+1)
    r%=MOD

nr=1
for i in range(W-1):
    nr*=(i+1)
    nr%=MOD

print(n%MOD*modinv(r*nr)%MOD)
