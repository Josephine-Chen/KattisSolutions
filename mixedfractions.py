import math
while True:
  n, d = map(int, input().split())
  if n == 0 and d == 0:
    break
  r = n % d
  w = int(math.floor(n / d))
  print("{} {} / {}".format(w, r, d))
