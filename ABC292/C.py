import math

N = int(input())

ans=0
for AB in range(1, N):
    # ABの組み合わせ
    x=0
    for A in range(1, int(math.sqrt(AB))+1):
        if AB%A==0:
            x+=1
            if A*A!=AB:
                x+=1
    
    y=0
    CD=N-AB
    for C in range(1, int(math.sqrt(CD))+1):
        if CD%C==0:
            y+=1
            if C*C!=CD:
                y+=1
    
    ans+=x*y
print(ans)