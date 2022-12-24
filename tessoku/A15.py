from collections import defaultdict
import bisect

N = int(input())
A = list(map(int, input().split()))

# d=defaultdict(int)

# for a in A:
#     d[a]+=1

# d=sorted(d)

# B=[]
# for a in A:
#     index = bisect.bisect_left(d, a)
#     B.append(index+1)
# print(*B)

A_set=sorted(set(A))
for i in range(N):
    index=bisect.bisect_left(A_set, A[i])
    A[i]=index+1
print(*A)
