number = [int(x) for x in input().split()]


def exchange(command, index):
    left = number[:int(index) + 1]
    right = number[int(index) + 1:]
    new = right + left
    return new


def first_last_even_odd(com, count, typpe):
    com = command[0]
    counter = int(command[1])
    new_list = []
    typpe = command[2]
    if counter > len(number):
        return "Invalid count"
    if typpe == 'even':
        new_list = [x for x in number if x % 2 == 0]
    elif typpe == 'odd':
        new_list = [x for x in number if x % 2 != 0]
    first = new_list[:count]
    last = new_list[-count:]
    if counter > len(first) or counter > len(last):
        return new_list
    if len(new_list) == 0:
        return new_list
    if com == "first":
        return first
    else:
        return last


def max_min_even_odd(com, num_type):
    new_list = []
    if num_type == 'even':
        new_list = [x for x in number if x % 2 == 0]
    elif num_type == 'odd':
        new_list = [x for x in number if x % 2 != 0]
    if len(new_list) == 0:
        return "No matches"
    if com == 'max':
        return len(number) - 1 - number[::-1].index(max(new_list))
    elif com == 'min':
        return len(number) - 1 - number[::-1].index(min(new_list))


while True:

    command = input().split()
    if command[0] == 'end':
        break
    if command[0] == 'exchange':
        if not int(command[1]) in range(len(number)):
            print("Invalid index")
        else:
            number = exchange(number, command[1])
    elif command[0] == 'first':
        print(first_last_even_odd(number, int(command[1]), command[2]))
    elif command[0] == 'last':
        print(first_last_even_odd(number, int(command[1]), command[2]))
    elif command[0] == 'max':
        print(max_min_even_odd(command[0], command[1]))
    elif command[0] == 'min':
        print(max_min_even_odd(command[0], command[1]))
print(number)