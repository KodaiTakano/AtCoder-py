N = int(input())
A = list(map(int, input().split()))

sum_front=[0]
crr=0
for a in A:
    crr=max(crr, a)
    sum_front.append(crr)

sum_back=[0]
crr=0
for i in range(N):
    crr=max(crr, A[N-i-1])
    sum_back.append(crr)

# print(sum_front)
# print(sum_back)

D = int(input())
for _ in range(D):
    L, R = map(int, input().split())
    print(max(sum_front[L-1], sum_back[N-R]))