N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

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
    AN=0
    for a in A:
        if a<=mid:
            AN+=1
    BN=0
    for b in B:
        if b>=mid:
            BN+=1
    if AN>=BN:
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
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    return ok

print(binary_search(-1, max(max(B), max(A))+1))