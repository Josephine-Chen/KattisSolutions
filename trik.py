def move(ball, cup1, cup2):
  if ball == cup1:
    return cup2
  elif ball == cup2:
    return cup1
  else:
    return ball

tricks = input()
pos = 1
for trick in tricks:
  if trick == 'A':
    pos = move(pos, 1, 2)
  elif trick == 'B':
    pos = move(pos, 2, 3)
  else:
    pos = move(pos, 1, 3)
print(pos)
