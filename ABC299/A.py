N = int(input())
S = list(input())
from sys import exit
c=0
for s in S:
    if s=="|":
        c+=1
    
    if c==1 and s=="*":
        print("in")
        exit()
print("out")