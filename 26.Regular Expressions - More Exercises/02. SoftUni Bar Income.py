import re

valid_order_old = r'^%([A-Z][a-z]+)%(?:[^\.\|\$%]+)?<(\w+)>(?:[^\.\|\$%]+)?\|(\d+)\|(?:[^\.\|\$%]+)?((?<=\D)\d+(?:\.\d+)?\$)'
valid_order = r'^%([A-Z][a-z]+)%(?:[^\.\|\$%]+)?<(\w+)>(?:[^\.\|\$%]+)?\|(\d+)\|(?:[^\.\|\$%]+)?((?<=\D)\d+(?:\.\d+)?)(?=\$)\$$'
income = 0

while True:
    text_input = input()
    if text_input == 'end of shift':
        break

    match = re.search(valid_order,text_input)

    if match:
        customerName = match.group(1)
        product = match.group(2)
        quantity = int(match.group(3))
        price = float(match.group(4))
        totalPrice = quantity * price
        print(f"{customerName}: {product} - {totalPrice:.2f}")
        income += totalPrice

print(f'Total income: {income:.2f}')