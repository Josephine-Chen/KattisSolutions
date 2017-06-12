lines = list()
longest = 0
while True:
  try:
    n = input()
    lines.append(n)
    if len(n) > longest:
      longest = len(n)
  except EOFError:
    break
lines = lines[:-1]
total = 0
for line in lines:
  total += (len(line)-longest) ** 2
print(total)
