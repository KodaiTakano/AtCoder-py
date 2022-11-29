N = int(input())

keta=len(str(N))
ans=(N-10**(keta-1)+1)*(keta//3)

for i in range(keta-1):
    ans+=9*(10**i)*(i//3)
    # print(ans)
print(ans)