N = int(input())
B = [[0]*1500 for _ in range(1500)]
# print(B)
for _ in range(N):
    x, y = map(int, input().split())
    B[x-1][y-1]+=1
# for i in range(10):
#     print(B[i][:10])
# print()

sum=[[0]*(1500+1)]
for i in range(1500):
    s=[0]
    crr=0
    for j in range(1500):
        crr+=B[i][j]
        s.append(crr+sum[i][j+1])
    sum.append(s)
    # if i<12:
    #     print(s[:11])

# print(len(sum), len(sum[1]))
Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(sum[c][d]-sum[a-1][d]-sum[c][b-1]+sum[a-1][b-1])