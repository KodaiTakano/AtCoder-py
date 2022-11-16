import sys

R, N, M = map(int, input().split())

if N**2+M**2<R**2:
    print(2)
    sys.exit()

ans=0
while(1):
    if N**2+M**2 <= (R*ans)**2:
        print(ans)
        sys.exit()
    ans+=1

