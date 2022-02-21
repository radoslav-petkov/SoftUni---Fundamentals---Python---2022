PCs = {}
products = []
inputline = input()
while inputline != 'END':
    tmp = inputline.split(' ')
    if tmp[0] == 'ADDPC':
        PCs[tmp[1]] = 'None'
    elif tmp[0] == 'REMOVEPC':
        PCs.pop(tmp[1], None)
    elif tmp[0] == 'ADDPRODUCT':
        PCs[tmp[1]] = str(PCs[tmp[1]])+str(PCs[tmp[2]])
    elif tmp[0] == 'REMOVEPRODUCT':
        print('REMOVEPRODUCT')
    elif tmp[0] == 'PRINT':
        print('PRINT')
    else:
        cikal = True
        while cikal:
            products.append(inputline)
            inputline = input()
            if inputline == 'PC':
                cikal = False
    inputline = input()
print(products)