import math

N, M = map(int, input().split())

ans=1000000000000000
for a in range(1, 10000000):
    if M%a==0:
        b=int(M/a)
    else:
        b=int(M/a)+1
        
    # if a>3:
    #     break

    # print(a, b)

    if a>N:
        continue
    
    if b>N:
        continue
    
    ans=min(ans, a*b)

if ans==1000000000000000:
    print(-1)
else:
    print(ans)