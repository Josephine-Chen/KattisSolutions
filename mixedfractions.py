import math
while True:
  n, d = map(int, input().split())
  if n == 0 and d == 0:
    break
  r = n % d
  w = int(math.floor(n / d))
  print("{} {} / {}".format(w, r, d))

  # Another method. Slower. Top takes .04s, bottom takes .05s
  
  while True:
  n, d = map(int, input().split())
  if n == 0 and d == 0:
    break
  f = divmod(n, d)
  print('{} {} / {}'.format(f[0], f[1], d))
