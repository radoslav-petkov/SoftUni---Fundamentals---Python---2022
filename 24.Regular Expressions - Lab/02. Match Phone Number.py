import re

input_string = input()
match_pattern = r'(\+359)([\s-])(2\2\d{3}\2\d{4}\b)'
matches = re.findall(match_pattern,input_string)
output_list = [m[0] + m[1] + m[2] for m in matches]
output = ', '.join(output_list)
print(output)