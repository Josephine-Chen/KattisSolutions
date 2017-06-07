def checkSum(n):
  ind = len(n) - 1
  s = sum(n[:ind])
  if s != n[ind]:
    ind -= 1
    while ind >= 0:
      s = sum(n[:ind]) + sum(n[(ind + 1):])
      if s != n[ind]:
        ind -= 1
      else:
        return n[ind]
  else:
    return n[ind]
import sys
for lines in sys.stdin.readlines():
  n = sorted(map(int, lines.split()))
  print(checkSum(n))
