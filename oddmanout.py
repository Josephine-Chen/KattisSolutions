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
