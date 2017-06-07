import math
n = int(input())
for i in range(n):
  v, a, x, h1, h2 = map(float, input().split())
  t = x/(v * math.cos(math.radians(a)))
  y = v * t * math.sin(math.radians(a)) - .5 * 9.81 * t ** 2
  if y > h1 + 1 and y < h2 - 1:
    print('Safe')
  else:
    print('Not Safe')
