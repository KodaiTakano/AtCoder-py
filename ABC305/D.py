N = int(input())
A = list(map(int, input().split()))

s=[]
crr=0
for i in range(N):
    if i%2!=0:
        crr+=A[i+1]-A[i]
        s.append(crr)
    else:
        s.append(crr)
# print(A)
# print(s)

from bisect import bisect_left

Q  = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    # 寝てる時は偶数
    l_i=bisect_left(A, l)
    r_i=bisect_left(A, r)
    # print(l_i, r_i)
    if l_i%2==0:
        if r_i%2==0:
            print(s[r_i]-s[l_i]-(A[r_i]-r)+(A[l_i]-l))
        else:
            r_i-=1
            print(s[r_i]-s[l_i]+(A[l_i]-l))
    else:
        l_i-=1
        if r_i%2==0:
            print(s[r_i]-s[l_i]-(A[r_i]-r))
        else:
            r_i-=1
            print(s[r_i]-s[l_i])