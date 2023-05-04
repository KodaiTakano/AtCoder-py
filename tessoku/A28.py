N = int(input())
ans=0
for _ in range(N):
    a, b = input().split()
    if a=="+":
        ans+=int(b)
    elif a=="-":
        ans-=int(b)
    else:
        ans*=int(b)
    ans%=10000
    print(ans)