n, m = map(int, input().split())
if n >= m:
  for x in range(m + 1, n + 2):
    print(x)
else:
  for x in range(n + 1, m + 2):
    print(x)
