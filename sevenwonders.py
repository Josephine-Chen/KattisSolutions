cards = list(input())
t = cards.count('T')
c = cards.count('C')
g = cards.count('G')
if t > 0 and c > 0 and g > 0:
  sets = min(t, c, g)
else:
  sets = 0
total = t ** 2 + c ** 2 + g ** 2 + 7 * sets
print(total)
