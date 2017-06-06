n = int(input())
nsort = sorted(str(n))
nplus = n + 1
while True:
  new = sorted(str(nplus))
  if new == nsort:
    print(nplus)
    break
  elif len(new) > len(nsort):
    print(0)
    break
  else:
    nplus += 1
