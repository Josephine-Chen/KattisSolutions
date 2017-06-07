def checkAdrian(ans):
  score = 0
  for i in range(len(ans)):
    if i % 3 == 0 and ans[i] == 'A':
      score += 1
    elif i % 3 == 1 and ans[i] == 'B':
      score += 1
    elif i % 3 == 2 and ans[i] == 'C':
      score += 1
  return score
def checkBruno(ans):
  score = 0
  for i in range(len(ans)):
    if (i % 4 == 0 or i % 4 == 2) and ans[i] == 'B':
      score += 1
    elif i % 4 == 1 and ans[i] == 'A':
      score += 1
    elif i % 4 == 3 and ans[i] == 'C':
      score += 1
  return score

def checkGoran(ans):
  score = 0
  for i in range(len(ans)):
    if (i % 6 == 0 or i % 6 == 1) and ans[i] == 'C':
      score += 1
    elif (i % 6 == 2 or i % 6 == 3) and ans[i] == 'A':
      score += 1
    elif (i % 6 == 4 or i % 6 == 5) and ans[i] == 'B':
      score += 1
  return score

n = int(input())
answers = input()
adrian = checkAdrian(answers)
bruno = checkBruno(answers)
goran = checkGoran(answers)
maxScore = max(adrian, bruno, goran)
print(maxScore)
if adrian == maxScore:
  print('Adrian')
if bruno == maxScore:
  print('Bruno')
if goran == maxScore:
  print('Goran')
