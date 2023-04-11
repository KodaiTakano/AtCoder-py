from sys import exit
N = int(input())
S = list(input())

place=[0,0]
A=set()
A.add(str(place))
for s in S:
    if s=="R":
        place[0]+=1
    elif s=="L":
        place[0]-=1
    elif s=="U":
        place[1]+=1
    else:
        place[1]-=1
    if str(place) in A:
        print("Yes")
        exit()
    A.add(str(place))
print("No")