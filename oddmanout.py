n = int(input())
caseNum = 1
for i in range(n):
  g = int(input())
  guests = list(map(int, input().split()))
  uniq = set(guests)
  for code in uniq:
    if guests.count(code) == 1:
      print("Case #" + str(caseNum) + ": " + str(code))
  caseNum += 1

  # Faster. Above takes 0.17s. Below takes 0.04s.
n = int(input())
for i in range(n):
    g = int(input())
    c = sorted(list(map(int, input().split())))
    found = False
    for j in range(0, g - 1, 2):
        if c[j] != c[j + 1]:
            found = True
            break
    if found:
        print('Case #{}: {}'.format(i + 1, c[j]))
    else:
        print('Case #{}: {}'.format(i + 1, c[-1]))
