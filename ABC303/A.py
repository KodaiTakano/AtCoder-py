from sys import exit

N = int(input())
S = list(input())
T = list(input())

for i in range(N):
    if S[i]!=T[i]:
        if S[i]=="1" or S[i]=="l":
            if T[i]!="1" and T[i]!="l":
                print("No")
                exit()
        elif S[i]=="0" or S[i]=="o":
            if T[i]!="0" and T[i]!="o":
                print("No")
                exit()
        else:
            print("No")
            exit()
print("Yes")
        