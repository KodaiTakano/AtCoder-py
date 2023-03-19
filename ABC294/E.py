L, N1, N2 = map(int, input().split())

v1=[]
l1=[]
for i in range(N1):
    N, M = map(int, input().split())
    v1.append(N)
    l1.append(M)

v2=[]
l2=[]
for i in range(N2):
    N, M = map(int, input().split())
    v2.append(N)
    l2.append(M)

s1=[0]
sum=0
for i in range(N1):
    sum+=l1[i]
    s1.append(sum)
s2=[0]
sum=0
for i in range(N2):
    sum+=l2[i]
    s2.append(sum)
print(*s1)
print(*s2)

