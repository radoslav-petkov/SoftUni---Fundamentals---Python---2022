input_string = input()

emoticon_list = [str(input_string[i:i+2]) for i in range(len(input_string)-1) if input_string[i] == ':']
if emoticon_list:
    for item in emoticon_list:
        print(item)