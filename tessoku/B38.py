N = int(input())
S = list(input())

a_c=[1]
streak=1
for i in range(N-1):
    if S[i]=="A":
        streak+=1
    else:
        streak=1
    a_c.append(streak)

b_c=[1]
streak=1
for i in range(N-2, -1, -1):
    if S[i]=="B":
        streak+=1
    else:
        streak=1
    b_c.append(streak)

# print(a_c)
# print(b_c)

ans=0
for i in range(N):
    ans+=max(a_c[i], b_c[N-i-1])
print(ans)