MOD = 1000000007
N = int(input())
ans=1
for i in range(N):
    A = list(map(int, input().split()))
    ans*=sum(A)%MOD

print(ans%MOD)