from math import factorial

N, L = map(int, input().split())
MOD = 1000000007

facN=[1]*100001
for i in range(1, 100001):
    facN[i]=facN[i-1]*i

ans=0
for i in range((N//L)+1):
    ans+=facN[N-i*L+i]//(facN[i]*facN[N-i*L])
print(ans%MOD)