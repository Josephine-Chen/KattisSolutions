import math
n, w, h = map(int, input().split())
maxl = h ** 2 + w ** 2
maxl = math.sqrt(maxl)
for num in range(n):
  m = int(input())
  if m <= maxl:
    print('DA')
  else:
    print('NE')
