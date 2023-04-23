# def is_ok(mid):
#     """二分探索中の判定

#     Parameters
#     ----------
#     mid : int

#     Returns
#     -------
#     result : bool
#     答えが左にある(ok=midにしたい)ときはTrue
#     答えが右にある(ng=midにしたい)ときはFalse
#     """
#     count=0
#     for a in A:
#         count+=mid//a
#     if M<=count:
#         return True
#     else:
#         return False

def binary_search(ng, ok):
    """二分探索

    Parameters
    ----------
    ng : int 初期値は(最小値-1)
    ok : int 初期値は(最大値+1)

    Returns
    -------
    ok : int
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2

        # print(ok, ng, mid)
        print("?", mid)
        n = int(input())
        if n:
            ok = mid
        else:
            ng = mid

    return ng

N = int(input())
print("!", binary_search(0, N))