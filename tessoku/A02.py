import sys

N, X = map(int, input().split())
A = list(map(int, input().split()))

for a in A:
    if a==X:
        print("Yes")
        sys.exit()
print("No")