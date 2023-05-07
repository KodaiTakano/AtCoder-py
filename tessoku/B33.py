N, H, W = map(int, input().split())

A=[]
B=[]
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a-1)
    B.append(b-1)
    

a_ans=A[0]
for i in range(1, N):
    a_ans^=A[i]

b_ans=B[0]
for i in range(1, N):
    b_ans^=B[i]


if a_ans^b_ans==0:
    print("Second")
else:
    print("First")