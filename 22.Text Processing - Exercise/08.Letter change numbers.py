alphabet = 'abcdefghijklmnopqrstuvwxyz'
char_num = lambda x: alphabet.find(x.lower()) + 1

input_strings  = [x for x in input().split()]
output = 0

for word in input_strings:
    first_char_num = char_num(word[0])
    last_char_num = char_num(word[-1])
    number_in_word = int(word[1:-1])

    if word[0].isupper():
        number_in_word /= first_char_num
    elif word[0].islower():
        number_in_word *= first_char_num

    if word[-1].isupper():
        number_in_word -= last_char_num
    elif word[-1].islower():
        number_in_word += last_char_num

    output += number_in_word

print ('{:.2f}'.format(output))