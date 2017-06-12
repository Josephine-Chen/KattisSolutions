n = int(input())
names = list()
for i in range(n):
  names.append(input())
incr = sorted(names)
decr = sorted(names,key=None,reverse=True)
if names == incr:
  print('INCREASING')
elif names == decr:
  print('DECREASING')
else:
  print('NEITHER')
