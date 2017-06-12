import sys
dupe = list()
for line in sys.stdin.readlines():
  n = line.split()
  wasteless = ''
  for i in range(len(n)):
    if n[i].lower() in dupe:
      wasteless += '. '
    else:
      dupe.append(n[i].lower())
      wasteless += n[i] + ' '
  print(wasteless.strip())

#Another way to solve
dupe = list()
while True:
  try:
    eff = list()
    n = input().split()
    for i in range(len(n)):
      if n[i] in dupe:
        eff.append('.')
      else:
        dupe.append(n[i])
        eff.append(n[i])
    print(eff)
  except EOFError:
    break
