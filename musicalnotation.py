def addNotes(note, sheet):
  duration = 1
  staff = ['G', 'F', 'E','D','C','B','A','g','f','e','d','c','b','a']
  if len(note) == 2:
    duration = int(note[1])
  for i in range(duration):
    ind = staff.index(note[0])
    sheet[ind] += '*'
    sheet = addPad(sheet, ind)
  return sheet
def addPad(sheet, ignore):
  lines = [1, 3, 5, 7, 9, 13]
  spaces = [0, 2, 4, 6, 8, 10, 11, 12]
  for line in lines:
    sheet[line] += '-'
  for space in spaces:
    sheet[space] += ' '
  if ignore != -1:
    sheet[ignore] = sheet[ignore][:-1]
  return sheet

n = int(input())
notes = input().split()
sheet = ['','','','','','','','','','','','','','']
for i in range(len(notes)):
  sheet = addNotes(notes[i], sheet)
  if i != (len(notes) - 1):
    sheet = addPad(sheet, -1)
print("G: {}\nF: {}\nE: {}\nD: {}\nC: {}\nB: {}\nA: {}\ng: {}\nf: {}\ne: {}\nd: {}\nc: {}\nb: {}\na: {}".format(sheet[0], sheet[1], sheet[2], sheet[3], sheet[4], sheet[5], sheet[6], sheet[7], sheet[8], sheet[9], sheet[10], sheet[11], sheet[12], sheet[13]))
