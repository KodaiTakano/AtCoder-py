H, W = map(int, input().split())
B = [list(input()) for _ in range(H)]


add_i=0
done=0
A=[]
for i in range(H):
    if B[i]!=["."]*W:
        A.append(B[i])
        done=1
    elif done==0:
        add_i+=1
AH=len(A)        
# [print(*A[i]) for i in range(len(A))]

A = [list(x) for x in zip(*A)]
# [print(*A[i]) for i in range(AH)]

# print()

add_j=0
done=0
C=[]
for j in range(W):
    # print(A[j])
    # print(["."]*AH)
    if A[j]!=["."]*AH:
        C.append(A[j])
        done=1
    elif done==0:
        add_j+=1

# [print(*C[i]) for i in range(len(C))]
C = [list(x) for x in zip(*C)]

# print(add_i)
# print(add_j)
# [print(*C[i]) for i in range(len(C))]

for i in range(len(C)):
    for j in range(len(C[i])):
        if C[i][j]==".":
            print(i+add_i+1, j+add_j+1)