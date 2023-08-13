H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]

hc=[]
for i in range(H):
    c=0
    for j in range(W):
        if S[i][j]==".":
            c+=1
    hc.append(c)

wc=[]
for j in range(W):
    c=0
    for i in range(H):
        if S[i][j]==".":
            c+=1
    wc.append(c)
# print(hc)
# print(wc)

for _ in range(K):
    l=hc+wc
    # print(l)
    max_index=l.index(max(l))
    if max_index<H:
        for j in range(W):
            if S[max_index][j]==".":
                S[max_index][j]="#"
                hc[max_index]-=1
                wc[j]-=1
    else:
        max_index-=H
        for i in range(H):
            if S[i][max_index]==".":
                S[i][max_index]="#"
                hc[i]-=1
                wc[max_index]-=1

ans=0
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            ans+=1
print(ans)