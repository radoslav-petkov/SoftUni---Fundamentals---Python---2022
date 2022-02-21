price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
type_items = input()
left_damage = 0
right_damage = 0
value_entry_point = price_ratings[entry_point]
left_items = price_ratings[:entry_point]
right_items = price_ratings[entry_point + 1:]
position = ""

if type_items == "cheap":
    for i in left_items:
        if i < value_entry_point:
            left_damage += i
    for i in right_items:
        if i < value_entry_point:
            right_damage += i
elif type_items == "expensive":
    for i in left_items:
        if i >= value_entry_point:
            left_damage += i
    for i in right_items:
        if i >= value_entry_point:
            right_damage += i

if right_damage > left_damage:
    position = "Right"
    print(f"{position} - {right_damage}")
else:
    position = "Left"
    print(f"{position} - {left_damage}")

