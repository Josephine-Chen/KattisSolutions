def danger(hero):
  if (hero % (a + b) > 0) and (hero % (a + b) <= a):
    if (hero % (c + d) > 0) and (hero % (c + d) <= c):
      print('both')
    else:
      print('one')
  else:
    if (hero % (c + d) > 0) and (hero % (c + d) <= c):
      print('one')
    else:
      print('none')
a, b, c, d = map(int, input().split())
p, m, g = map(int, input().split())
danger(p)
danger(m)
danger(g)
