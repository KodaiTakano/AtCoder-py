A, B, W = map(int, input().split())
W*=1000

is_OK=False
for i in range(1000001):
    if A*i<=W and W<=B*i:
        is_OK=True
        break

if is_OK==False:
    print("UNSATISFIABLE")
else:
    # 最小値から考える
    # Bがb個あってWにピッタリか足りてないか
    if W%B==0:
        min = W//B
    else:
        min = W//B+1
    # Aがa個あってピッタリか超えてるか
    max = W//A
    print(min, max)