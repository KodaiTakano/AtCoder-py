N = int(input())
S = list(input())
from sys import exit

e=0
for s in S:
    if s=="o":
        e=1
    if s=="x":
        print("No")
        exit()
if e==1:
    print("Yes")
else:
    print("No")