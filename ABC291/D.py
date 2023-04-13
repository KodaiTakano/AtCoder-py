N = int(input())
A=[]
B=[]
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
# print(A, B)
MOD = 998244353

# # count[0]:下の出現回数, count[0][0]:下の表の出現回数, count[1]:次の上の出現回数
# count = [[0, 0],[0, 0]]
# ans = 0
# for i in range(N-2):
#     if A[i]!=A[i+1]:
#         count[0][0]+=1
#     if A[i]!=B[i+1]:
#         count[0][1]+=1
#     if B[i]!=A[i+1]:
#         count[0][0]+=1
#     if B[i]!=B[i+1]:
#         count[0][1]+=1

#     if A[i+1]!=A[i+2]:
#         count[1][0]+=1
#     if A[i+1]!=B[i+2]:
#         count[1][0]+=1
#     if B[i+1]!=A[i+2]:
#         count[1][1]+=1
#     if B[i+1]!=B[i+2]:
#         count[1][1]+=1
#     print(i, count)
#     ans+=count[0][0]*count[1][0]+count[0][1]*count[1][1]
#     ans%=MOD

#     count = [[0, 0],[0, 0]]
# print(ans)

# dp[i][flag]: i枚目のカードまでの表裏の決め方のうち、条件を満たし、i枚目のカードが表裏であるような方法の数
dp=[[0,0] for _ in range(N)]
dp[0]=[1,1]

for i in range(1, N):
    if A[i-1]!=A[i]:
        dp[i][0]+=dp[i-1][0]
    if A[i-1]!=B[i]:
        dp[i][1]+=dp[i-1][0]
    if B[i-1]!=A[i]:
        dp[i][0]+=dp[i-1][1]
    if B[i-1]!=B[i]:
        dp[i][1]+=dp[i-1][1]
    
    dp[i][0]%=MOD
    dp[i][1]%=MOD

print((dp[N-1][0]+dp[N-1][1])%MOD)