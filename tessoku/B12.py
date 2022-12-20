N = int(input())

def is_ok(mid):
    """二分探索中の判定

    Parameters
    ----------
    mid : int

    Returns
    -------
    result : bool
    答えが左にある(ok=midにしたい)ときはTrue
    答えが右にある(ng=midにしたい)ときはFalse
    """

    if N<=mid**3+mid:
        return True
    else:
        return False

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
    while abs(ok - ng) > 0.00001:
        mid = (ok + ng) / 2
        # print(ng, mid, ok)
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    # print(ok, mid, ng)
    return ok

print("{:.5f}".format(binary_search(-1, 10**5+1)))