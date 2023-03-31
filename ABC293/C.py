import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

def dfs(x, y, num:set):
    global ans
    if A[x][y] in num:
        return
    
    if x==H-1 and y==W-1:
        ans+=1
    
    num.add(A[x][y])
    
    if x<H-1:
        dfs(x+1, y, num)
    if y<W-1:
        dfs(x, y+1, num)
    num.discard(A[x][y])

num=set()
ans=0
dfs(0, 0, num)
print(ans)