new_list = input().split(" ")
num_comands = int(input())



for data in range(num_comands):
    current = input(data).split(" ")
    comand = current[0]
    if comand == 'Include':
        index1 = current[1]
        new_list.append(index1)
    if comand == 'Remove':
        index2 = int(current[2])
        index1 = current[1]
        if index1 == 'last':
            new_list.pop(-1)
        else:
            new_list = new_list[index2:]
    if comand == 'Prefer':
        index1 = int(current[1])
        index2 = int(current[2])
        new_list[index1],new_list[index2] = new_list[index2], new_list[index1]

    if comand == 'Reverse':
        new_list.reverse()


print('Coffees:')
result = (' '.join(new_list))
print(result)
