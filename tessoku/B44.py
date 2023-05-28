N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# i行目にline[i]行がある
line = list(range(N))

Q = int(input())
for i in range(Q):
    B = list(map(int, input().split()))
    if B[0]==1:
        temp=line[B[1]-1]
        line[B[1]-1]=line[B[2]-1]
        line[B[2]-1]=temp
    else:
        print(A[line[B[1]-1]][B[2]-1])
    
    # print(line)