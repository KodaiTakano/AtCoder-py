N = int(input())
A = list(map(int, input().split()))

tA=sorted(A)
print(A.index(tA[N-1])+1)