import re
input_text = input()
email_pattern = re.compile(r'(^|(?<=\s))[a-zA-Z0-9]+[\w\.-]+@[a-zA-Z0-9]+[a-zA-Z0-9-]+\.[a-zA-Z]+(\.[a-zA-Z]+)?')
matches = email_pattern.finditer(input_text)
for m in matches:
    print(m.group(0))