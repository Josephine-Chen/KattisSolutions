for i in range(int(input())):
  turtles = list(map(int, input().split()))
  turtles = turtles[:-1]
  imported = 0
  for i in range(1, len(turtles)):
    imported += max(0, turtles[i] - 2 * turtles[i - 1])
  print(imported)
