fires_cells = input().split('#')
water_amount = int(input())

effort = 0
total_fire = 0
condition = False

print('Cells:')
for current_fire in fires_cells:
    fire_info = current_fire.split(' = ')
    type_of_fire = fire_info[0]
    value_of_fire = int(fire_info[1])
    condition = False

    if type_of_fire == 'High':
        if 81 <= value_of_fire <= 125:
            condition = True

    elif type_of_fire == 'Medium':
        if 51 <= value_of_fire <= 80:
            condition = True

    elif type_of_fire == 'Low':
        if 1 <= value_of_fire <= 50:
            condition = True

    if condition:
        if water_amount >= value_of_fire:
            water_amount -= value_of_fire
            effort += value_of_fire * 0.25
            total_fire += value_of_fire
            print(f' - {value_of_fire}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire? {total_fire}')




# cells = input().split('#')
# water_amount = int(input())
#
# HIGH_RANGE = range(81, 126)
# MEDIUM_RANGE = range(51, 81)
# LOW_RANGE = range(1, 51)
#
# effort = 0
# putout_fires = []
#
# for cell in cells:
#     fire_type, fire_value = cell.split(' = ')
#     fire_value = int(fire_value)
#
#     if fire_type == 'High' and fire_value not in HIGH_RANGE:
#         continue
#
#     elif fire_type == 'Medium' and fire_value not in MEDIUM_RANGE:
#         continue
#
#     elif fire_type == 'Low' and fire_value not in LOW_RANGE:
#         continue
#
#     if water_amount >= fire_value:
#         water_amount -= fire_value
#         effort += fire_value * 0.25
#         putout_fires.append(fire_value)
#
# print('Cells:')
# for cell in putout_fires:
#     print(f' - {cell}')
# print(f'Effort: {effort:.2f}')
# print(f'Total Fire: {sum(putout_fires)}')
