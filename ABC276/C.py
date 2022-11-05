N = int(input())
P = list(map(int, input().split()))

change_index=0
for i in range(1, N):
    if P[N-i]-P[N-1-i] < 0:
        change_index=N-i-1
        break

swap_index=0
swap_num=10000
for i in range(change_index+1, N):
    if P[change_index]-P[i] >0 and P[change_index]-P[i] < swap_num:
        swap_index=i
        swap_num=P[change_index]-P[i]
# print(swap_num)
# print(swap_index)

P[change_index], P[swap_index] = P[swap_index], P[change_index]
        
        
tempP=sorted(P[change_index+1:], reverse=True)
P[change_index+1:N] = tempP
print(*P)