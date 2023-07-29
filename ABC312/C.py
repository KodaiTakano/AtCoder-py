N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

from collections import defaultdict
AD=defaultdict(int)
for a in A:
    AD[a]+=1
BD=defaultdict(int)
for b in B:
    BD[b]+=1
CD=defaultdict(int)
for a in A:
    CD[a]+=1
for b in B:
    CD[b]+=1
CD = sorted(CD.items())
# print(CD)

from sys import exit

AN=0
BN=M
for k, v in CD:
    AN+=AD[k]
    BN-=BD[k]
    if AN>=BN:
        if AD[k]==0:
            print(k+1)
        else:
            print(k)
        exit()