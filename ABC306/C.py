N = int(input())
A = list(map(int, input().split()))

count=[0]*N

for i in range(3*N):
    # print()
    # print(count)
    count[A[i]-1]+=1
    if count[A[i]-1]==2:
        print(A[i], end=" ")
    