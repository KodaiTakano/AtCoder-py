N, Q = map(int, input().split())
A = list(map(int, input().split()))
count=0
for i in range(Q):
    print(A)
    T, x, y = map(int, input().split())
    if T==1:
        x=(x-count-1)%N
        y=(y-count-1)%N
        temp=A[x]
        A[x]=A[y]
        A[y]=temp
    elif T==2:
        count+=1   
    else:
        print(A[(x-count-1)%N])
        
# print(-1%8)