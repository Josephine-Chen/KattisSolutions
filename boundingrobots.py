while True:
  w, l = map(int, input().split())
  if w == 0 and l == 0:
    break
  n = int(input())
  robot = [0,0]
  actual = [0,0]
  for i in range(n):
    walk = input().split()
    direction = walk[0]
    dist = int(walk[1])
    if direction == 'u':
      actual[1] += dist
      if robot[1] + dist > l - 1:
        robot[1] = l - 1
      else:
        robot[1] += dist
    elif direction == 'd':
      actual[1] -= dist
      if robot[1] - dist < 0:
        robot[1] = 0
      else:
        robot[1] -= dist
    elif direction == 'r':
      actual[0] += dist
      if robot[0] + dist > w - 1:
        robot[0] = w - 1
      else:
        robot[0] += dist
    else:
      actual[0] -= dist
      if robot[0] - dist < 0:
        robot[0] = 0
      else:
        robot[0] -= dist
  print('Robot thinks {} {}'.format(actual[0], actual[1]))
  print('Actually at {} {}'.format(robot[0], robot[1]))
  print('')
