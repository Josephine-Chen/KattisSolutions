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
