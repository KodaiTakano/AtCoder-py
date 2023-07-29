N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
# print(S)

def is_ok(x, y):
    ok=True
    for i in range(9):
        for j in range(9):
            # print(i, j)
            # print(ok)
            if i<3 and j<3:
                if S[x+i][y+j]!="#":
                    ok=False
            if i>6 and j>6:
                if S[x+i][y+j]!="#":
                    ok=False
            
            if i==3 and j<4:
                if S[x+i][y+j]!=".":
                    ok=False
            if i<4 and j==3:
                if S[x+i][y+j]!=".":
                    ok=False
            if i==5 and j>5:
                if S[x+i][y+j]!=".":
                    ok=False
            if i>5 and j==5:
                if S[x+i][y+j]!=".":
                    ok=False
    return ok

ans=[]
for x in range(N-8):
    for y in range(M-8):
        if is_ok(x, y):
            ans.append([x+1, y+1])
    #     break
    # break

[print(*ans[i]) for i in range(len(ans))]
            