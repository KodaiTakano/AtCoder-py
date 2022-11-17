H, W, X, Y = map(int, input().split())
B = [list(input()) for _ in range(H)]

ans=1
for i in range(X-1, H):
    if B[i][Y-1]==".":
        ans+=1
        # print(i, Y-1)
    else:
        break
for i in range(1, X+1):
    if B[X-i][Y-1]==".":
        ans+=1
        # print(X-i, Y-1)
    else:
        break
for i in range(Y-1, W):
    if B[X-1][i]==".":
        ans+=1
        # print(X-1, i)
    else:
        break
for i in range(1, Y+1):
    if B[X-1][Y-i]==".":
        ans+=1
        # print(X-1, Y-i)
    else:
        break
print(ans-4)