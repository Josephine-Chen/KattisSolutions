n = int(input())
for i in range(n):
  message = input()
  secret = ''
  l = len(message)
  k = 1
  while k ** 2 < l:
    k += 1
  m = k ** 2
  message += '*' * (m - l)
  grid = [[''] * k for j in range(k)]
  for i in range(m):
    row = i // k
    col = i % k
    grid[row][col] = message[0]
    message = message[1:]
  grid = grid[::-1]
  for l in range(k):
    for j in range(k):
      secret += grid[j][l]
  secret = secret.replace('*', '')
  print(secret)
