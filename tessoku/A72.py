import itertools

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

import copy

ans=0
for pro in itertools.product((0, 1), repeat=H):
    tempS=copy.deepcopy(S)
    temphc=hc.copy()
    tempwc=wc.copy()
    
    c=0
    for p in pro:
        if p==1:
            c+=1
    if c>K:
        continue

    for i in range(len(pro)):
        if pro[i]==1:
            for j in range(W):
                if tempS[i][j]==".":
                    tempS[i][j]="#"
                    temphc[i]-=1
                    tempwc[j]-=1
    
    for _ in range(K-c):
        max_index=tempwc.index(max(tempwc))
        for i in range(H):
            if tempS[i][max_index]==".":
                tempS[i][max_index]="#"
                temphc[i]-=1
                tempwc[max_index]-=1
    
    count=0
    for i in range(H):
        for j in range(W):
            if tempS[i][j]=="#":
                count+=1
    ans=max(ans, count)

print(ans)                    
                    
# (0, 0, 0)
# (0, 0, 1)
# (0, 1, 0)
# (0, 1, 1)
# (1, 0, 0)
# (1, 0, 1)
# (1, 1, 0)
# (1, 1, 1)

# hc=[]
# for i in range(H):
#     c=0
#     for j in range(W):
#         if S[i][j]==".":
#             c+=1
#     hc.append(c)

# wc=[]
# for j in range(W):
#     c=0
#     for i in range(H):
#         if S[i][j]==".":
#             c+=1
#     wc.append(c)
# # print(hc)
# # print(wc)

# for _ in range(K):
#     l=hc+wc
#     # print(l)
#     max_index=l.index(max(l))
#     if max_index<H:
#         for j in range(W):
#             if S[max_index][j]==".":
#                 S[max_index][j]="#"
#                 hc[max_index]-=1
#                 wc[j]-=1
#     else:
#         max_index-=H
#         for i in range(H):
#             if S[i][max_index]==".":
#                 S[i][max_index]="#"
#                 hc[i]-=1
#                 wc[max_index]-=1

# ans=0
# for i in range(H):
#     for j in range(W):
#         if S[i][j]=="#":
#             ans+=1
# print(ans)