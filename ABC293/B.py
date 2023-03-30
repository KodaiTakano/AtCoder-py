N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))

# # 呼ばれてない人
# B=set(range(0, N))
# for i in range(N):
#     if i in B:
#         B.discard(A[i])
# print(len(B))
# for b in B:
#     print(b+1, end=" ")
    
B=[0]*N
for i in range(N):
    if B[i]==0:
        B[A[i]]=1

ans=0
for b in B:
    if b==0:
        ans+=1
print(ans)
for i in range(N):
    if B[i]==0:
        print(i+1, end=" ")