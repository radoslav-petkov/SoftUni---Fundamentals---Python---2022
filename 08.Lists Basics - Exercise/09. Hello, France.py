CLOTHES_MAX_PRICE = 50.0
SHOES_MAX_PRICE = 35.0
ACCESSORIES_MAX_PRICE = 20.50
TARGET_MONEY = 150.0

items = input().split('|')
budget = float(input())


items_bought = []
profit = 0

for item in items:
    item_type, item_price = item.split('->')
    item_price = float(item_price)

    if item_type == 'Clothes' and item_price > CLOTHES_MAX_PRICE:
        continue

    elif item_type == 'Shoes' and item_price > SHOES_MAX_PRICE:
        continue

    elif item_type == 'Accessories' and item_price > ACCESSORIES_MAX_PRICE:
        continue

    if budget < item_price:
        continue

    budget -= item_price
    current_profit = item_price * 0.4
    profit += current_profit
    items_bought.append(item_price+current_profit)


print(' '.join([format(price, '.2f') for price in items_bought]))

print(f'Profit: {profit:.2f}')

if budget + sum(items_bought) >= TARGET_MONEY:
    print('Hello, France!')
else:
    print('Not enough money.')






# items = input().split('|')
# budget = int(input())
# profit = 0
# new_item_prices = []
# data_prices = []
# condition = False
#
# for item in items:
#     current_item_info = item.split('->')
#     type_of_product = current_item_info[0]
#     price = float(current_item_info[1])
#     condition = False
#
#     if type_of_product == 'Clothes':
#         if price <= 50:
#             condition = True
#     elif type_of_product == 'Shoes':
#         if price <= 35:
#             condition = True
#     elif type_of_product == 'Accessories':
#         if price <= 20.50:
#             condition = True
#
# if condition:
#     if budget >= price:
#         budget -= price
#         profit += price * 0.40
#         new_price = price + (price * 0.40)
#         new_item_prices.append(new_price)
#         data_prices.append(f'{new_price:.2f}')
#
# print(' '.join(data_prices))
# print(f'Profit: {profit:.2f}')
#
# total_sum = budget + sum(new_item_prices)
#
# if total_sum >= 150:
#     print('Hello, France!')
# else:
#     print('Not enough money.')


