txt_input = input()

print(''.join([ch for ch in txt_input if ch.isdigit()]))
print(''.join([ch for ch in txt_input if ch.isalpha()]))
print(''.join([ch for ch in txt_input if not (ch.isdigit() or ch.isalpha()) ]))