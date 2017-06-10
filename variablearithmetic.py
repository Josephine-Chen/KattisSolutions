import re
var = dict()
equal = False
while True:
  n = input()
  if n == '0':
    break
  if '=' in n:
    n = re.sub('=', '', n)
    n = n.split()
    var[n[0]] = int(n[1])
    equal = True
  else:
    n = re.sub(r'[^\w]', ' ', n)
    n = n.split()
  nums = 0
  strs = list([])
  for i in n:
    if i.isdigit():
      nums += int(i)
    else:
      if i in var:
        nums += int(var[i])
      else:
        strs.append(i)
  if nums != 0 and len(strs) != 0 and equal == False:
    print(str(nums) + ' + '+ ' + '.join(strs))
  elif nums == 0 and equal == False:
    print(' + '.join(strs))
  elif len(strs) == 0 and equal == False:
    print(str(nums))
  equal = False
