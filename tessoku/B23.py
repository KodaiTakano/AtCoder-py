# def base_n(num_10, n):
#     if num_10==0:
#         return 0
#     str_n = ''
#     while num_10:
#         if num_10%n>=10:
#             return -1
#         str_n += str(num_10%n)
#         num_10 //= n
#     return int(str_n[::-1])

# from math import sqrt

# def dist(A:list, B:list):
#     return sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)

# N = int(input())
# # 都市座標[[x0, y0],[x1, y1],...]
# A=[]
# for _ in range(N):
#     a = list(map(float, input().split()))
#     A.append(a)
# # print(A)

# # dp[S][j]: Sが通った都市、jが今いる都市で最短の時間
# # どの都市からスタートしても同じため、都市0からスタートする
# # Sは集合(set) 0:2^0 1:2^1 01:2^0+2^1 2:2^2

# # 今jで次にkに行く時
# # dp[S+k][k]=min(dp[S+k][k], dp[S][j]+dist(j, k))
# dp=[[1000000000]*(2^(N+1)) for _ in range(N+1)]

# dp[0][0]=0
# for s in range(2^N):
#     for j in range(N):
#         if dp[s][j]>=1000000000:
#             continue
#         place=set()
#         TWO = list(str(base_n(s, 2)))
#         TWO.reverse()
#         for i in range(len(TWO)):
#             if TWO[i]=="1":
#                 place.add(i+1)
#         print(s, place)
#         # 都市jからkに移動する
#         for k in range(N):
#             # 都市kを通ってたとき
#             if k in place:
#                 continue
#             print(k)
#             dp[s+2^k][k]=min(dp[s+2^k][k], dp[s][j]+dist(A[j], A[k]))

# print(dp[2^N-1][0])