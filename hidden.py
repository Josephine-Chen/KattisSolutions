p, s = input().split()
init = -1
fail = False
for i in range(len(p)):
  ind = s.find(p[i])
  if p.count(p[i]) > 1:
    s = s[:ind] + s[(ind + 1):]
  if ind == -1 or ind < init:
    fail = True
    break
  else:
    init = ind
if fail == True:
  print('FAIL')
else:
  print('PASS')
