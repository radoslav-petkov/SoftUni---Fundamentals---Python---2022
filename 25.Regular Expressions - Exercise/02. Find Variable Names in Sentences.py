import re
text = input()
pattern = re.compile(r'(^|(?<=\s))_([a-zA-Z0-9]+(?=\s|$))')
matches = re.finditer(pattern,text)

output = [m.group(2) for m in matches]
print(','.join(output))