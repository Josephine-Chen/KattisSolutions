import re
names = input()
search = re.findall(r'[A-Z]', names)
print(''.join(search))
