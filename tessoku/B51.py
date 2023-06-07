from collections import deque

q=deque()
S = list(input())

ans=[]
for i in range(len(S)):
    if S[i]=="(":
        q.append(i+1)
    else:
        ans.append([q[-1],i+1])
        q.pop()

for i in range(len(ans)):
    ans[i].append(max(ans[i][0],ans[i][1]))
ans = sorted(ans, reverse=False, key=lambda x: x[2]) #0列目を基準にして昇順ソート
for i in range(len(ans)):
    print(ans[i][0], ans[i][1])