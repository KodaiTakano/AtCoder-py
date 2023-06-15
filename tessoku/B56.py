N, Q = map(int, input().split())
S = list(input())

# 右半分と左半分の文字列が一致しているかどうかハッシュ値で確認する
# 左から右のL[i](S[0:i]のハッシュ値)を求める
# 同様に右から左のR[i](S[N:N-i]のハッシュ値)を求める
# l,rが与えられた時にl~(l+r)/2のハッシュ値と(l+r)/2~rのハッシュ値が一致してるかどうか

MOD = 1000000007

# 文字を数字化
abc = "abcdefghijklmnopqrstuvwxyz"
for i in range(N):
    S[i]=abc.index(S[i])+1

# L[i]:S[0~i-1]までのハッシュ化
L=[0]
for i in range(N):
    L.append((100*L[i]+S[i])%MOD)

# R[i]:S[N~N-i]までのハッシュ化
R=[0]
for i in range(N):
    R.append((100*R[i]+S[N-i-1])%MOD)

# print(L)
# print(R)

# B[i]:100^i
B=[1]
for i in range(1, N+1):
    B.append(B[i-1]*100%MOD)

# S[l]~S[r]のハッシュ値はH[r]-B^(r-l+1)*H[l-1]
for _ in range(Q):
    A = list(map(int, input().split()))
    l=A[0]
    r=A[1]
    m=(l+r)//2
    if (l+r)%2==0:
        # l~m
        HL=L[m]-(B[m-l+1]*L[l-1])%MOD
        if HL<0:
            HL+=MOD
        # Rのabs(N+1-r)~abs(N+1-m)
        # print(abs(N+1-r),abs(N+1-m))
        HR=R[abs(N+1-m)]-(B[abs(N+1-m)-abs(N+1-r)+1]*R[abs(N+1-r)-1])%MOD
        if HR<0:
            HR+=MOD
    else:
        # Lのl~m
        HL=L[m]-(B[m-l+1]*L[l-1])%MOD
        if HL<0:
            HL+=MOD
        # Rのabs(N+1-r)~abs(N+1-(m+1))
        # print(abs(N+1-r),abs(N+1-(m+1)))
        HR=R[abs(N+1-(m+1))]-(B[abs(N+1-(m+1))-abs(N+1-r)+1]*R[abs(N+1-r)-1])%MOD
        if HR<0:
            HR+=MOD
    if HL==HR:
        print("Yes")
    else:
        print("No")
        
    