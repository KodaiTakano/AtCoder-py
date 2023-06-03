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
UF=UnionFind(N)
for i in range(M):
    u, v = map(int, input().split())
    UF.unite(u-1, v-1)

# iのルートノードを格納
Root=[]
for i in range(N):
    Root.append(UF.root(i))

K = int(input())
# xyのルートノードを格納
Rootxy=[set() for _ in range(2*10**5)]
for _ in range(K):
    x, y = map(int, input().split())
    Rootxy[Root[x-1]].add(Root[y-1])
    Rootxy[Root[y-1]].add(Root[x-1])
# print(Rootxy)

Q  = int(input())
for _ in range(Q):
    p, q = map(int, input().split())
    p_root=UF.root(p-1)
    q_root=UF.root(q-1)
    # print(p_root, q_root)
    if q_root in Rootxy[p_root]:
        print("No")
    else:
        print("Yes")