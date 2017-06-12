import re
n = int(input())
for i in range(n):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  p = input()
  p = re.sub('\W', '', p)
  p = re.sub('\d', '', p)
  for i in range(len(p)):
    if p[i].lower() in alpha:
      alpha = alpha.replace(p[i].lower(), '')
  if len(alpha) == 0:
    print('pangram')
  else:
    print('missing {}'.format(alpha))
