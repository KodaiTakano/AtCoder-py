N = int(input())
H = list(map(int, input().split()))

A=[0]*N
A[1]=abs(H[0]-H[1])
for i in range(2, N):
    A[i]=min(A[i-1]+abs(H[i]-H[i-1]), A[i-2]+abs(H[i]-H[i-2]))
# print(A)
ans=[N]
index=N-1
while(1):
    if index==0:
        break
    if index==1:
        ans.append(index)
        break
    if A[index]-abs(H[index]-H[index-1])==A[index-1]:
        ans.append(index)
        index-=1
    else:
        ans.append(index-1)
        index-=2
print(len(ans))
print(*reversed(ans))