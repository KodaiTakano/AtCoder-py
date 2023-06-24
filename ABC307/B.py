N = int(input())
S = [list(input()) for _ in range(N)]

from sys import exit

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        tempS=S[i]+S[j]
        SN=len(tempS)
        if SN%2==0:
            if tempS[:int(len(tempS)/2)]==list(reversed(tempS[int(len(tempS)/2):])):
                    print("Yes")
                    exit()
        else:
            # print(tempS[:int(len(tempS)/2)], list(reversed(tempS[int(len(tempS)/2)+1:])))
            if tempS[:int(len(tempS)/2)]==list(reversed(tempS[int(len(tempS)/2)+1:])):
                    print("Yes")
                    exit()
print("No")