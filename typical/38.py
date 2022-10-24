import math


N, M = map(int, input().split())

g = math.gcd(N, M)
print(g)
ans=N//g
print(ans)
print(10**18//M)
if ans <= 10**18//M:
    print(ans*M)
else:
    print("Large")