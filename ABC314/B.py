N = int(input())
C=[]
A=[]
for i in range(N):
    c = int(input())
    C.append(c)
    a = list(map(int, input().split()))
    A.append(a)
X = int(input())


me=1000
ans=[]
for i in range(N):
    for j in range(C[i]):
        if A[i][j]==X:
            if C[i]<me:
                ans=[]
                ans.append(i+1)
                me = C[i]
            elif C[i]==me:
                ans.append(i+1)
print(len(ans))
for a in ans:
    print(a, end=" ")