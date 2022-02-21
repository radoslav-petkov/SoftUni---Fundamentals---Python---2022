inputline = input()
tempDict = {}
gotovi = 0
inputlinesplit = inputline.split(' -> ')
while gotovi!=3:
    if len(inputlinesplit) == 2:
        tempDict[inputlinesplit[0]] = inputlinesplit[1]
    elif len(inputlinesplit) == 1 and inputlinesplit[0] == 'STOP':
        first = tempDict.copy()
        tempDict.clear()
        gotovi+=1
    elif len(inputlinesplit) == 1 and inputlinesplit[0] == 'HALT':
        second =tempDict.copy()
        tempDict.clear()
        gotovi+=1
    elif len(inputlinesplit) == 1 and inputlinesplit[0] == 'END':
        third = tempDict.copy()
        tempDict.clear()
        gotovi+=1
    if gotovi == 3:
        break
    inputlinesplit = input().split(' -> ')
massage = input()
for bukva in first.keys():
    if bukva in massage:
        massage = massage.replace(bukva, first[bukva])
print(massage)
