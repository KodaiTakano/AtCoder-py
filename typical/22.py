import math

A, B, C = map(int, input().split())

g = math.gcd(A, B)
g = math.gcd(g, C)

A//=g
B//=g
C//=g
print(A+B+C-3)