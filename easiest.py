while True:
  n = int(input())
  if n == 0:
    break
  p = 11
  while sum(map(int, str(n))) != sum(map(int, str(n * p))):
    p += 1
  print(p)
