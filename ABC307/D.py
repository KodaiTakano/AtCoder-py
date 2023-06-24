N = int(input())
S = list(input())

# 消す範囲
delete=[]
# (の位置
l=[]

for i in range(N):
    # 最初の(
    if S[i]=="(":
        l.append(i)
    if l!=[] and S[i]==")":
        delete.append([l[-1], i])
        l.pop()
# print(delete)

delete = sorted(delete, reverse=False, key=lambda x: x[0]) #0列目を基準にして昇順ソート
# print(delete)

# print([list(x) for x in zip(*delete)])

import bisect

if delete!=[]:
    dTx=[list(x) for x in zip(*delete)][0]
# print(dTx)

id=0
inloop=0
for i in range(N):
    if delete==[]:
        print(S[i], end="")
        continue
    
    if delete[id][0]<=i<=delete[id][1]:
        if i==delete[id][1]:
            id = bisect.bisect_left(dTx, i+1)
            if id==len(dTx):
                id-=1
        continue
    else:
        # print(i)
        # print(id)
        print(S[i], end="")