N, D = map(int, input().split())

A=[]
for _ in range(N):
    B = list(map(int, input().split()))
    A.append(B)

A = sorted(A, reverse=False, key=lambda x: x[0])
# print(A)

ans=0
day=1
# すでに選ばれたindex
s=set()
while(day<=D):
    m=0
    index=N
    for i in range(N):
        # print(i)
        if A[i][0]<=day and i not in s:
            if m<A[i][1]:
                m=A[i][1]
                index=i
        if A[i][0]>day or i==N-1:
            ans+=m
            day+=1
            s.add(index)
            break
    # print(s)
    # print(ans)

print(ans)