N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]

A = sorted(B, reverse=True, key=lambda x: x[1])

a=A[0][1]
af=A[0][0]
b=-1
bf=-1
bi=-1
for i in range(N):
    if A[i][0]!=af:
        b=A[i][1]
        bf=A[i][0]
        bi=i
     
ans=0
for i in range(1, N):
    if A[i][0]==af:
        ans=max(ans, a+A[i][1]/2)
    else:
        ans=max(ans, a+A[i][1])
        
# for i in range(N):
#     if i!=bi:        
#         if A[i][0]==bf:
#             ans=max(ans, b+A[i][1]/2)
#         else:
#             ans=max(ans, b+A[i][1])
print(int(ans))
