X, Y = map(int, input().split())

ans=[[X, Y]]
while(X!=1 or Y!=1):
    if X<Y:
        Y-=X
        ans.append([X, Y])
    else:
        X-=Y
        ans.append([X, Y])
ans.reverse()
print(len(ans)-1)
[print(*ans[i]) for i in range(1, len(ans))]