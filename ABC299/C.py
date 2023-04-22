from sys import exit
N = int(input())
S = list(input())

if "-" not in S:
    print(-1)
    exit()

ans=0
count=0
for i in range(N):
    if S[i]=="o":
        count+=1
    # print(count)
    if i==N-1:
        ans=max(ans, count)
    if S[i]=="-":
        ans=max(ans, count)
        count=0


if ans==0:
    print(-1)
else:
    print(ans)