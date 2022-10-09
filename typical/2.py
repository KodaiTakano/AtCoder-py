import itertools

N = int(input())

if N%2==0:
    l = []
    for i in range(N):
        l.append(i)
    for v in itertools.combinations(l, int(N/2)):
        sum=0
        isOK = True
        for i in range(N):
            if i in v:
                sum+=1
            else:
                sum-=1
            if sum<0:
                isOK = False
                break
        if isOK == True:
            for i in range(N):
                if i in v:
                    print("(", sep="", end="")
                else:
                    print(")", sep="", end="")
            print("")