import re

intpu_string = input()
re_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
matches = re.findall(re_pattern,intpu_string)
output = ' '.join(matches)
print(output)