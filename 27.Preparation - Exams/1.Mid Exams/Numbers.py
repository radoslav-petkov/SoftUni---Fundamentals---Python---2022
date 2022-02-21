num_list = [int(x) for x in input().split()]

data = input()
while not data == 'Finish':

    command = data.split()[0]
    number = int(data.split()[1])
    if command == "Add":
        num_list.append(number)
    elif command == 'Remove':
        num_list.remove(number)
    elif command == "Replace":
        replacement = int(data.split()[2])
        index_loc = num_list.index(number)
        num_list.remove(number)
        num_list.insert(index_loc, replacement)
    elif command == "Collapse":
        for nums in num_list[::-1]:
            if nums < number:
                num_list.remove(nums)
    data = input()

print(' '.join([str(x) for x in num_list]))