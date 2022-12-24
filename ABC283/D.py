# from collections import defaultdict
# import sys

# S = list(input())

# d=defaultdict(int)
# l=[]
# s=[]
# for i in range(len(S)):
#     if S[i]==")":
#         l.append(s)
#         s=[]
#         for i in range(len(l[len(l)-1])):
#             # print("----", l[len(l)-1][i])
#             d[l[len(l)-1][i]]=0
#         l.pop()
#     elif S[i]=="(":
#         l.append(s)
#         s=[]
#     # 文字だったとき
#     else:
#         if d[S[i]]==1:
#             print("No")
#             sys.exit()
#         d[S[i]]=1
#         s.append(S[i])
#     print(d)
#     print(l)
#     print(s)
# print("Yes")

import sys

S = list(input())

l=set()
for i in range(len(S)):
    if S[i]==")":
        l.clear()
    elif S[i]!="(":
        if S[i] in l:
            print("No")
            sys.exit()
        l.add(S[i])
print("Yes")