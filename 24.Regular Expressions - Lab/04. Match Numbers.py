import re
input_string = input()
match_pattern = r'(^|(?<=\s))-?(0(\.d+)?|[1-9](\d+)?(\.\d+)?)($|(?=\s))'

matches = re.finditer(match_pattern,input_string)
for m in matches:
    print(m.group(0), end=' ')