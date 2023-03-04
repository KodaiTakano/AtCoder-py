N, Q = map(int, input().split())

A=[0]*N

for i in range(Q):
    a, b = map(int, input().split())
    if a==1:
        A[b-1]+=1
    elif a==2:
        A[b-1]+=2
    elif a==3:
        if A[b-1]>=2:
            print("Yes")
        else:
            print("No")