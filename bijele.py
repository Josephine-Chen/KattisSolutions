[k, q, r, b, n, p] = map(int, input().split())
mset = [k, q, r, b, n, p]
cset = [1, 1, 2, 2, 2, 8]
nset = [0, 0, 0, 0, 0, 0]
for x in range(6):
  nset[x] = cset[x] - mset[x]
  nset[x] = str(nset[x])
print(' '.join(nset))
