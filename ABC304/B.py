from decimal import Decimal,ROUND_DOWN

N = int(input())
D='1E'+str(len(str(N))-3)
# print(D)
if N<1000:
    print(N)
else:
    print(int(Decimal(N).quantize(Decimal(D), rounding=ROUND_DOWN)))