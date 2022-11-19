N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [list(map(int, input().split())) for _ in range(Q)]
add={}
alla=-1
for i in range(Q):
    if B[i][0]==1:
        alla=B[i][1]
        add={}
    if B[i][0]==2:
        if B[i][1]-1 in add:
            add[B[i][1]-1]+=B[i][2]
        else:
            add[B[i][1]-1]=B[i][2]
    if B[i][0]==3:
        if alla == -1:
            if B[i][1]-1 in add:
                print(A[B[i][1]-1]+add[B[i][1]-1])
            else:
                print(A[B[i][1]-1])
        else:
            if B[i][1]-1 in add:
                print(alla+add[B[i][1]-1])
            else:
                print(alla)
    # print(add, alla)