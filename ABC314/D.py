N = int(input())
S = list(input())
Q = int(input())

# 全部大文字かどうか
allB=0
# 小文字のindex
Sm=set()

allS=0
Bi=set()

for i in range(Q):
    A = list(input().split())
    # print(i, Sm, Bi)
    if A[0]=="1":
        S[int(A[1])-1]=A[2]
        if A[2].islower():
            if int(A[1])-1 in Bi:
                Bi.remove(int(A[1])-1)
            Sm.add(int(A[1])-1)
        if A[2].isupper():
            if int(A[1])-1 in Sm:
                Sm.remove(int(A[1])-1) 
            Bi.add(int(A[1])-1)

    elif A[0]=="2":
        allB=0
        allS=1
        Sm=set()
        Bi=set()
    else:
        allB=1
        allS=0
        Bi=set()
        Sm=set()

if allB:
    for i in range(N):
        if i in Sm:
            print(S[i].lower(), end="")
        else:
            print(S[i].upper(), end="")
elif allS:
    for i in range(N):
        if i in Bi:
            print(S[i].upper(), end="")
        else:
            print(S[i].lower(), end="")
else:
    # for i in range(N):
    print(*S, sep="")
    