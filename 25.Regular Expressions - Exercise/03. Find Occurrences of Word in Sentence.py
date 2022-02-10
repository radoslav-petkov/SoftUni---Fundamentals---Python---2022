import re

text = input()
word = input()

pattern = rf'\b{word}\b'

matches = re.findall(pattern,text,flags=re.IGNORECASE)

print(len(matches))