input_string = input()
index = 0
explosion = 0

while index < len(input_string):
    char = input_string[index]
    if input_string[index] == '>':
        explosion += int(input_string[index + 1])
        index += 1

    elif explosion > 0:
        input_string =  input_string[:index] + input_string[index + 1:]
        explosion -= 1

    else:
        index += 1
else:
    print(input_string)