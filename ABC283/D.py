from collections import deque
import sys

S = list(input())

l=[[]]
ball=set()
for i in range(len(S)):
    if S[i]==")":
        for x in l[len(l)-1]:
            ball.remove(x)
        l.pop()
    elif S[i]=="(":
        l.append([])
    # 文字だったとき
    else:
        if S[i] in ball:
            print("No")
            sys.exit()
        ball.add(S[i])
        l[len(l)-1].append(S[i])
    # print(l)
    # print(ball)
print("Yes")

# 嘘解法
# import sys

# S = list(input())

# l=set()
# for i in range(len(S)):
#     if S[i]==")":
#         l.clear()
#     elif S[i]!="(":
#         if S[i] in l:
#             print("No")
#             sys.exit()
#         l.add(S[i])
# print("Yes")