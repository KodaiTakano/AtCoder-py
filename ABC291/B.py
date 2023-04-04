N = int(input())
A = sorted(list(map(int, input().split())))

sum=0
for i in range(N, 4*N):
    sum+=A[i]
print(sum/(3*N))