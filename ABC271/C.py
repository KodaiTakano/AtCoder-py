import collections

N = int(input())
A = sorted(map(int, input().split()))

D:dict = collections.Counter(A)
trash=[]
erase=[]
for i in D:
    # print(i)
    if(i>N):
        erase.append(i)
        for j in range(D[i]):
            trash.append(i)
            D[i]-=1
    if(D[i]>=2):
        for j in range(D[i]-1):
            trash.append(i)
            D[i]-=1

for i in erase:
    D.pop(i)

# print(trash)
# print(dict(D))

for i in range(N):
    # print(i)
    if(i+1 in D):
        D.pop(i+1)
    else:
        if(len(trash)>=2):
            trash=trash[:-2]
        elif(len(trash)==1 and len(D)>=1):
            trash=[]
            D.popitem()
        else:
            print(i)
            break
