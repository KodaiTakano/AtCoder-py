N, Q = map(int, input().split())
S = list(input())

MOD = 1000000007

# (ハッシュ値)=100^(N-1)*S[0]+100^(N-2)*S[1]...+100^0*S[N-1]

# 文字を数字化
abc = "abcdefghijklmnopqrstuvwxyz"
for i in range(N):
    S[i]=abc.index(S[i])+1

# H[i]:S[0,i]までのハッシュ化
H=[0]
for i in range(N):
    H.append((100*H[i]+S[i])%MOD)

# B[i]:100^i
B=[1]
for i in range(1, N+1):
    B.append(B[i-1]*100%MOD)

# S[l]~S[r]のハッシュ値はH[r]-B^(r-l+1)*H[l-1]
for _ in range(Q):
    A = list(map(int, input().split()))
    a=A[0]
    b=A[1]
    c=A[2]
    d=A[3]
    H1=H[b]-(B[b-a+1]*H[a-1])%MOD
    if H1<0:
        H1+=MOD
    H2=H[d]-(B[d-c+1]*H[c-1])%MOD
    if H2<0:
        H2+=MOD
    if H1==H2:
        print("Yes")
    else:
        print("No")