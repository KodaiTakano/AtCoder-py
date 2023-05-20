class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
          self.par[x] = self.root(self.par[x]) # 経路圧縮
          return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

N, M = map(int, input().split())

S=[]
for _ in range(N):
    s = list(input())
    S.append(s)

G = [[] for _ in range(N)]
UF=UnionFind(N)

for i in range(N):
    for j in range(i+1, N):
        diff=0
        for k in range(M):
            if S[i][k]!=S[j][k]:
                diff+=1
        if diff==1:
            G[i].append(j)
            G[j].append(i)
            UF.unite(i, j)
# print(G)
from sys import exit

# グラフが連結してるかどうかの確認
if UF.size(0)!=N:
    print("No")
    exit()

# 準オイラーグラフの確認
c=0
for i in range(N):
    if len(G[i])==0:
        print("No")
        exit()
    if len(G[i])%2==1:
        c+=1
if c%2==0:
    print("Yes")
else:
    print("No")