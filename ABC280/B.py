N = int(input())
S = list(map(int, input().split()))

A=0
for i in S:
    print(i-A, end=" ")
    A+=(i-A)
    # print("A:", A)