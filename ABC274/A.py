from decimal import Decimal, ROUND_HALF_UP

A, B = map(int, input().split())

print('{:.3f}'.format(float(Decimal(str(B/A)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))))