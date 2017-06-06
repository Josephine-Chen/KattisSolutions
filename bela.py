dom = {'A': 11,
'K': 4,
'Q': 3,
'J': 20,
'T': 10,
'9': 14,
'8': 0,
'7': 0}
nonDom = {'A': 11,
'K': 4,
'Q': 3,
'J': 2,
'T': 10,
'9': 0,
'8': 0,
'7': 0}
n, b = input().split()
total = 0
for i in range(int(n) * 4):
  card = input()
  if card[1] == b:
    total += dom[card[0]]
  else:
    total += nonDom[card[0]]
print(total)
