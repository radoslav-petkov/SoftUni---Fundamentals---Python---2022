import re

parser = re.compile(r'(?<=<title>)(.+)(?=</title>)|((?:(?<=\>)|(?<=\\n))[^\\<]+(?:(?=\<)|(?=\\n)))')

input_string = input()

parsed_data = parser.finditer(input_string)

output_title = ''
output_content = ''
for data in parsed_data:
    if data.group(1):
        output_title += data.group(1)
    elif data.group(2):
        output_content += data.group(2)

print(f"Title: {output_title}")
print(f"Content: {output_content}")