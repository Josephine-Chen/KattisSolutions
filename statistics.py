import sys
caseNum = 1
for line in sys.stdin.readlines():
    C, *case = map(int, line.split())
    print("Case {}: {} {} {}".format(caseNum, min(case), max(case), max(case) - min(case)))
    caseNum += 1
