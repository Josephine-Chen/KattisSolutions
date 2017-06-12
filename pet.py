winner = [0, 0]
for x in range(5):
  scores = map(int, input().split())
  total = sum(i for i in scores)
  if total > winner[1]:
    winner[0] = x
    winner[1] = total
winner[0] += 1
print(winner[0], winner[1])

#Another method. Above takes .02s. Below takes .03s
contestants = list()
for i in range(5):
  p = sum(list(map(int, input().split())))
  contestants.append(p)
maxScore = max(contestants)
winner = str(contestants.index(maxScore) + 1)
print(winner + ' ' + str(maxScore))
