import sys
import bisect
import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))
before=A[:N//2]
after=A[N//2:]

before_sum=[]
for pro in itertools.product((0, 1), repeat=N//2):
    sum=0
    for i in range(N//2):
        if pro[i]==1:
            sum+=before[i]
    before_sum.append(sum)

after_sum=[]
for pro in itertools.product((0, 1), repeat=len(after)):
    sum=0
    for i in range(len(pro)):
        if pro[i]==1:
            sum+=after[i]
    after_sum.append(sum)
after_sum=sorted(after_sum)

for i in before_sum:
    index=bisect.bisect_left(after_sum, K-i)
    if index<len(after_sum) and after_sum[index]==K-i:
        print("Yes")
        sys.exit()

print("No")