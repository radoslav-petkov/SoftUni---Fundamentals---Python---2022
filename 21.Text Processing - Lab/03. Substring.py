remove_string = input()
text_string = input()

while remove_string in text_string:
    text_string = text_string.replace(remove_string,'')
else:
    print(text_string)