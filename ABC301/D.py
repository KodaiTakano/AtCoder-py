def base_n(num_10, n):
    if num_10==0:
        return 0
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return str_n[::-1]

def base_10(num_n, n):
    num_10 = 0
    for s in num_n:
        if s==2:
            continue
        num_10 *= n
        num_10 += int(s)
    return num_10

from sys import exit

S = list(input())
N = int(input())

ansl=[2]*len(S)
for i in range(len(S)):
    if S[i]=="1":
        ansl[i]=1
    if S[i]=="0":
        ansl[i]=0

N-=base_10(ansl, 2)
if N<0:
    print(-1)
    exit()
N2=list(map(int, list(base_n(N, 2))))

# print(ansl)
# print(N2)

if len(ansl)<len(N2):
    for _ in range(len(N2)-len(ansl)):
        ansl.insert(0, 0)
if len(ansl)>len(N2):
    for _ in range(len(ansl)-len(N2)):
        N2.insert(0, 0)

for i in range(len(ansl)):
    if ansl[i]==2:
        if N2==1:
            ansl[i]=1
        else:
            ansl[i]=0
    if ansl[i]==0 and N2[i]==1 and i!=len(ansl)-1:
        for j in range(i+1, len(ansl)):
            if ansl[j]==2:
                ansl[j]=1
        break

print(base_10(ansl, 2))