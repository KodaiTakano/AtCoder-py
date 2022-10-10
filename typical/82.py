# a%MOD*modinv(b)%MOD
def modinv(b, mod=10**9+7):
    return pow(b, mod-2, mod)

L, R = map(int, input().split()) 
MOD = 1000000007

L_digit=len(str(L))
R_digit=len(str(R))

ans=0
for i in range(L_digit, R_digit+1):
    ans=ans%MOD+((i*((10**i)*(10**i-1)%MOD-(10**(i-1))*(10**(i-1)-1)%MOD)*modinv(2))%MOD)%MOD
ans=ans%MOD-((L_digit*((L)*(L-1)%MOD-(10**(L_digit-1))*(10**(L_digit-1)-1)%MOD)*modinv(2))%MOD)%MOD
ans=ans%MOD-((R_digit*((10**R_digit)*(10**R_digit-1)%MOD-(R+1)*(R)%MOD)*modinv(2))%MOD)%MOD

print(int(ans%MOD))