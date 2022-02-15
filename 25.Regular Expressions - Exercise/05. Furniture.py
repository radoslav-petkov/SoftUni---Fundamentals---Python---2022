import re

# r'^>>([a-zA-Z]+)<<(\d+(\.\d{2})?)!(\d+)$'
valid_pattern = re.compile(r'^>>([a-zA-Z]+)<<(\d+(\.\d+)?)!(\d+)$')
bought_furniture = []
total_cost = 0

while True:
    input_text = input()
    if input_text == 'Purchase':
        break

    match = valid_pattern.search(input_text)
    if match:
        bought_furniture.append(match.group(1))
        total_cost += float(match.group(2)) * int(match.group(4))

print('Bought furniture:')
for item in bought_furniture:
    print(item)
print(f'Total money spend: {total_cost:.2f}')