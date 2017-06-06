winner = [0, 0]
for x in range(5):
  scores = map(int, input().split())
  total = sum(i for i in scores)
  if total > winner[1]:
    winner[0] = x
    winner[1] = total
winner[0] += 1
print(winner[0], winner[1])
