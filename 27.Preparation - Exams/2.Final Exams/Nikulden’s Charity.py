def replace(text, current, new):
    if current in text:
        text = text.replace(current, new)
    return text


def valid_index(text, start, end):
    if 0 <= start < len(text) and 0 <= end < len(text):
        return True
    return False


def cut(text, start, end):
    if valid_index(text, start, end):
        subst = text[start:end + 1]
        text = text.replace(subst, '')
        return text
    return False


def check(text, substring):
    if substring in text:
        return f'Message contains {substring}'
    else:
        return f'Message doesn\'t contain {substring}'


def sum_chars(text, start, end):
    substring = text[start:end + 1]
    result = 0
    for w in substring:
        result += ord(w)
    print(result)
    return text


initial_string = input()

while True:
    command = input()
    if command == 'Finish':
        break
    token = command.split()
    action = token[0]

    if action == 'Replace':
        current_char, new_char = token[1], token[2]
        initial_string = replace(initial_string, current_char, new_char)
        print(initial_string)

    elif action == 'Cut':
        start_index = int(token[1])
        end_index = int(token[2])
        if valid_index(initial_string, start_index, end_index):
            initial_string = cut(initial_string, start_index, end_index)
            print(initial_string)
        else:
            print(f'Invalid indexes!')

    elif action == 'Make':
        if token[1] == 'Upper':
            initial_string = initial_string.upper()
        elif token[1] == 'Lower':
            initial_string = initial_string.lower()
        print(initial_string)

    elif action == 'Check':
        string = token[1]
        print(check(initial_string, string))

    elif action == 'Sum':
        start_index = int(token[1])
        end_index = int(token[2])
        if valid_index(initial_string, start_index, end_index):
            sum_chars(initial_string, start_index, end_index)
        else:
            print('Invalid indexes!')

