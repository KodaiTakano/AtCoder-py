import sys

N, M = map(int, input().split())

for i in range(N, M+1):
    if 100%i==0:
        print("Yes")
        sys.exit()
print("No")