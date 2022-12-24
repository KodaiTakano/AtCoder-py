N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d=[0]*N
d[1]=A[0]
for i in range(2, N):
    d[i]=min(d[i-1]+A[i-1], d[i-2]+B[i-2])
    # print(d[i])
print(d[N-1])