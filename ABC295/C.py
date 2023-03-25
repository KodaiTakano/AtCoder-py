N = int(input())
A = sorted(list(map(int, input().split())))
# print(A)
count=1
ans=0
for i in range(1, N):
    # print("i=", i)
    # print(count)
    # print(ans)
    if A[i-1]==A[i]:
        count+=1
    else:
        ans+=int(count/2)
        count=1
print(ans+int(count/2))