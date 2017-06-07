def ingredients(r):
  ingr = []
  for i in range(r):
    ingredient = input().split()
    ingr.append(ingredient)
    if ingredient[2] == '100.0':
      main = ingredient
  return main, ingr

def weights(sw, ingredients, main):
  for i in range(len(ingredients)):
    if main == ingredients[i][0]:
      print(ingredients[i][0] + ' ' + str(sw))
    else:
      print(ingredients[i][0] + ' ' + str(round(float(ingredients[i][2]) * sw / 100, 1)))

t = int(input())
recipeNum = 1
for i in range(t):
  print('Recipe # ' + str(recipeNum))
  r, p, d = map(int, input().split())
  scaling = float(d) / p
  main, allIngredients = ingredients(r)
  scaledWeight = float(main[1]) * scaling
  weights(scaledWeight, allIngredients, main[0])
  print('-' * 40)
  recipeNum += 1
