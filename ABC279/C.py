import sys
from collections import defaultdict

H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]

S = [''.join(list(x)) for x in zip(*S)]
T = [''.join(list(x)) for x in zip(*T)]

dictS = defaultdict(int)
dictT = defaultdict(int)
for i in range(W):
    dictS[S[i]]+=1
    dictT[T[i]]+=1
dictS=sorted(dictS.items())
dictT=sorted(dictT.items())
# print(dictS)
# print(dictT)

for i in range(len(dictS)):
    if dictS[i]!=dictT[i]:
        print("No")
        sys.exit()
print("Yes")