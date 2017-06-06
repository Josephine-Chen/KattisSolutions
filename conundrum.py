text = input()
days = 0
for x in range(len(text)):
  if x % 3 == 0:
    if text[x] is not 'P':
      days += 1
  elif x % 3 == 1:
    if text[x] is not 'E':
      days += 1
  else:
    if text[x] is not 'R':
      days += 1
print(days)
