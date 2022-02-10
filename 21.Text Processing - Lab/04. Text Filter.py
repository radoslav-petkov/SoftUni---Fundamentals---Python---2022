ban_list = input().split(', ')
txt_string = input()

for word in ban_list:
    while word in txt_string:
        txt_string = txt_string.replace(word, '*' * len(word))

print(txt_string)