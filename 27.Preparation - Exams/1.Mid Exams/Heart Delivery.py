neighborhood = [int(el) for el in input().split('@')]
command = input()

position = 0

while not command == "Love!":
    length = int(command.split()[1])
    position += length

    if position < len(neighborhood):
        if neighborhood[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        else:
            neighborhood[position] -= 2
            if neighborhood[position] == 0:
                print (f"Place {position} has Valentine's day.")
    else:
        position = 0

        if neighborhood[position] == 0:
            print(f"Place {position} already had Valentine's day.")
        else:
            neighborhood[position] -=  2

    command = input()

print(f"Cupid's last position was {position}.")

if sum(neighborhood) == 0:
    print(f"Mission was successful.")
else:
    count = len([el for el in neighborhood if el > 0])
    print(f"Cupid has failed {count} places.")







# houses = input().split("@")
# command = input()
#
# position = 0
# failed = 0
#
# house = [int(el) for el in houses]
#
# while command != "Love!":
#
#     jump, length = command.split()
#     length = int(length)
#     position += length
#
#     if True:     # correct position
#         if position >= len(house):
#             position = 0
#         house[position] -= 2
#
#     if True:
#         if house[position] == 0:
#             print(f"Place {position} has Valentine's day.")
#
#         elif house[position] < 0:
#             print(f"Place {position} already had Valentine's day.")
#
#     command = input()
#
# for index in range(len(house)):
#     if house[index] > 0:
#         failed += 1
#
# print(f"Cupid's last position was {position}.")
#
# if failed == 0:
#     print("Mission was successful.")
# else:
#     print(f"Cupid has failed {failed} places.")







# house_list = [int(x) for x in input().split('@')]
#
# index = 0
# while True:
#     command = input()
#
#     if command == 'Love!':
#         break
#     else:
#         jump = int(list(command.split(' '))[1])
#         index += jump
#         if index >= len(house_list):
#             index = 0
#         if house_list[index] == 0:
#             print(f"Place {index} already had Valentine's day.")
#         else:
#             house_list[index] -= 2
#             if house_list[index] == 0:
#                 print(f"Place {index} has Valentine's day.")
#
# print(f"Cupid's last position was {index}.")
# if sum(house_list) == 0:
#     print('Mission was successful.')
# else:
#     failed_houses = [x for x in house_list if x != 0]
#     print(f'Cupid has failed {len(failed_houses)} places.')