import re
n = int(input())
cups = dict()
for i in range(n):
  cup = input().split()
  if re.match(r'\d', cup[0]):
    cups[cup[1]] = int(cup[0])/2
  else:
    cups[cup[0]] = int(cup[1])
cups = sorted(cups.items(), key = lambda x: x[1])
for j in range(len(cups)):
  print(cups[j][0])
