S = sorted(list(input()), reverse=True)
T = sorted(list(input()), reverse=True)

N=len(S)

sa=0
ta=0
for i in range(N):
    if S[i]=="@":
        sa+=1
    if T[i]=="@":
        ta+=1

from sys import exit
from collections import defaultdict
s = defaultdict(int)
t = defaultdict(int)

for i in range(N):
    s[S[i]]+=1
    t[T[i]]+=1

# print(s)
# print(t)

for sk, sv in s.items():
    if sk=="@":
        break
    t[sk]-=s[sk]

# print(t)

for tk, tv in t.items():
    if tk=="@":
        continue
    if tv!=0 and tk not in ["a", "t", "c", "o", "d", "e", "r"]:
        print("No")
        exit()
    if tv>0:
        if tv>sa:
            print("No")
            exit()
        sa-=tv
    if tv<0:
        if abs(tv)>ta:
            print("No")
        ta-=abs(tv)
print("Yes")