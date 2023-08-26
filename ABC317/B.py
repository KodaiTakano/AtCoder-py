N = int(input())
A = sorted(list(map(int, input().split())))

for i in range(N-1):
    if A[i]+1!=A[i+1]:
        print(A[i]+1)