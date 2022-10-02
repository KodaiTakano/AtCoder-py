N = int(input())
P1=[0]*(N+1)
P2=[0]*(N+1)
for i in range(N):
    C, P = map(int, input().split())
    if C==1:
        P1[i+1]=P
    else:
        P2[i+1]=P

s1=[0]
s2=[0]
for i in range(1, N+1):
    s1.append(s1[i-1]+P1[i])
    s2.append(s2[i-1]+P2[i])
# print(P1)
# print(s1)
# print(P2)
# print(s2)

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(s1[r]-s1[l-1], s2[r]-s2[l-1])
    