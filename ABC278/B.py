import sys
H, M = map(int, input().split())

def is_exist(a, b):
    tempa=a//10*10+b//10
    tempb=a%10*10+b%10
    if 0<=tempa and tempa<=23 and 0<=tempb and tempb<=59:
        return True
    else:
        return False

for i in range(H, 24):
    for j in range(0, 60):
        if i==H and j<M:
            continue
        if is_exist(i, j):
            print(i, j)
            sys.exit()

for i in range(0, 24):
    for j in range(0, 60):
        if is_exist(i, j):
            print(i, j)
            sys.exit()
