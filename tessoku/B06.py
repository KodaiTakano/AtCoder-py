N = int(input())
A = list(map(int, input().split()))

o=[0]
x=[0]
crr_o=0
crr_x=0
for a in A:
    if a==1:
        crr_o+=1
    else:
        crr_x+=1
    o.append(crr_o)
    x.append(crr_x)


Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    ans = o[R]-o[L-1]-(x[R]-x[L-1])
    if ans==0:
        print("draw")
    elif ans>0:
        print("win")
    else:
        print("lose")