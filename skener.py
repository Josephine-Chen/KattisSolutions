def handleRow(row, c, zc):
  tRow = ''
  for i in range(c):
    tRow += row[i] * zc
  print(tRow)
  return tRow

r, c, zr, zc = map(int, input().split())
for i in range(r):
  saved = handleRow(list(input()), c, zc)
  if zr > 1:
    for j in range(zr - 1):
      print(saved)
