N, X = map(int, input().split())
A = list(map(int, input().split()))
B = set(A)
from sys import exit

for a in A:
    if a+X in B:
        print("Yes")
        exit()
print("No")
