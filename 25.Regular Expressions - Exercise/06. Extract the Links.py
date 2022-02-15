import re

search_pattern = re.compile(r'www.[a-zA-Z0-9-]+(\.[a-z]+)+')

while True:
    input_text = input()
    if len(input_text) == 0:
        break
    matches = search_pattern.finditer(input_text)
    for match in matches:
        print(match.group(0))