input_string = input()


def find_next_char_index(i):
    if i == len(input_string) - 1:
        return i + 1
    else:
        while input_string[i] == input_string[i + 1]:
            i += 1
            if i == len(input_string) - 1:
                break
        return i + 1


output = ''
i = 0
while i < len(input_string):
    output += input_string[i]
    i = find_next_char_index(i)
else:
    print(output)
