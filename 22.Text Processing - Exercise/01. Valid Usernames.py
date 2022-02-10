import string

valid_chars = [ch for ch in list(string.printable) if ch.isalnum() or ch in ('-','_')]

lenght_valid = lambda x: True if 3 <= len(x) <= 16 else False

found_invalid_char = lambda x: True if list(filter(lambda ch: ch not in valid_chars,x)) else False

usernames = input().split(', ')
for name in usernames:
    if lenght_valid(name) and not found_invalid_char(name):
        print(name)