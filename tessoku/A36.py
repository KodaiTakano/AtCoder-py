from sys import exit

N, M = map(int, input().split())

if 2*(N-1)>M:
    print("No")
    exit()

if (2*(N-1)-M)%2==0:
    print("Yes")
    exit()
else:
    print("No")