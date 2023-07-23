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
A = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
# print(A)
B=set()
for i in range(M):
    B.add(1000000*A[i][0]+A[i][1])

UF=UnionFind(N)

# クエリ後に残る辺を調査
C=B
Q = int(input())
q = [list(map(lambda x: int(x)-1, input().split())) for _ in range(Q)]
for i in range(Q):
    # print(C)
    if q[i][0]==0:
        C.remove(1000000*A[q[i][1]][0]+A[q[i][1]][1])
for c in C:
    UF.unite(c%1000000, c//1000000)

ans=[]
for i in range(Q-1, -1, -1):
    if q[i][0]==0:
        UF.unite(A[q[i][1]][0], A[q[i][1]][1])
    else:
        if UF.issame(q[i][1], q[i][2]):
            ans.append("Yes")
        else:
            ans.append("No")

print(*reversed(ans), sep="\n")