N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d=[0]*N
d[1]=A[0]
root=[0]*N
for i in range(2, N):
    if d[i-1]+A[i-1]<d[i-2]+B[i-2]:
        d[i]=d[i-1]+A[i-1]
        root[i]=i-1
    else:
        d[i]=d[i-2]+B[i-2]
        root[i]=i-2
ans=[N]
index=N-1
while(root[index]!=0):
    ans.append(root[index]+1)
    index=root[index]
ans.append(1)
print(len(ans))
print(*reversed(ans))