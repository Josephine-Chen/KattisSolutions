import math
def distance(c1, c2):
  return math.sqrt((c1[0]-c2[0]) ** 2 + (c1[1]-c2[1]) ** 2)
m = int(input())
targets = list()
for i in range(m):
  shape, *coord = input().split()
  coord = list(map(int, coord))
  targets.append(coord)
n = int(input())
for j in range(n):
  hit = 0
  shot = list(map(int, input().split()))
  for target in targets:
    if len(target) == 3:
      if distance(shot, [target[0], target[1]]) <= target[2]:
        hit += 1
    else:
      if shot[0] >= target[0] and shot[0] <= target[2] and shot[1] >= target[1] and shot[1] <= target[3]:
        hit += 1
  print(hit)
