import sys
for line in sys.stdin.readlines():
  line = line.split()
  pl = ''
  for i in range(len(line)):
    yay = ['a', 'e', 'i', 'o', 'u', 'y']
    if line[i][0] in yay:
      pl += line[i] + 'yay '
    else:
      ind = []
      for vowel in yay:
        vow = line[i].find(vowel)
        if vow > 0:
          ind.append(vow)
      ind = min(ind)
      pl += line[i][ind:] + line[i][:ind] + 'ay '
  print(pl.strip())
