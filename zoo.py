listnum = 1
while True:
  n = int(input())
  if n == 0:
    break
  animalList = dict()
  for i in range(n):
    animal = input().split(' ')[-1].lower()
    if animal not in animalList:
      animalList[animal] = 1
    else:
      animalList[animal] += 1
  print('List ' + str(listnum) + ':')
  listnum += 1
  for anim in sorted(animalList.keys()):
    print(anim + ' | ' + str(animalList[anim]))
