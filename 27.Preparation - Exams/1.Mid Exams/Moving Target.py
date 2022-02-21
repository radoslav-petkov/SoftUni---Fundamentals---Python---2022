targets = input().split(" ")
targets = list(map(int, targets))

line = input()
while line != "End":
    command_list = line.split(" ")

    command = command_list[0]
    index = int(command_list[1])
    value = int(command_list[2])

    if command == "Shoot" and 0 <= index < len(targets):
        current_target = targets[index]
        current_target -= value

        if current_target <= 0:
            targets.pop(index)
        else:
            targets[index] = current_target

    elif command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        if index - value >= 0 and index + len(targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")

    line = input()

targets = list(map(str, targets))
output = "|".join(targets)
print(output)








# numbers = [int(el) for el in input().split()]
# text = input()
#
# while not text == "End":
#     command, index, power = text.split()
#     index = int(index)
#     power = int(power)
#
#     if "Shoot" in text:
#         if 0 <= index < len(numbers):
#             numbers[index] -= power
#             if numbers[index] <= 0:
#                 numbers.pop(index)
#
#     elif "Add" in text:
#         if 0 <= index < len(numbers):
#             numbers.insert(index, power)
#         else:
#             print("Invalid placement!")
#
#     elif "Strike" in text:
#         minimum = index - power
#         maximum = index + power
#
#         if minimum >= 0 and maximum < len(numbers):
#             del numbers[minimum: maximum + 1]
#         else:
#             print("Strike missed!")
#
#     text = input()
#
# print('|'.join(list(map(str, numbers))))







# def moving_target(data): #[52 74 23 44 96 110]
#     command = input()
#
#     while 'End' not in command:
#         command_sequence = command.split(' ')
#         element = command_sequence[0]
#         index = int(command_sequence[1])
#         value = int(command_sequence[2])
#
#         if element == 'Shoot' and index in range(len(data)): # Shoot 5 10
#             new_data = int(data[index]) - value
#             if new_data <= 0:
#                 data.pop(index)
#             else:
#                 data.pop(index)
#                 data.insert(index, str(new_data))
#
#         elif element == 'Add':
#             if index in range(len(data)):
#                 data.insert(index, str(value))
#             else:
#                 print("Invalid placement!")
#
#         elif element == 'Strike': # Strike 2 3
#             for i in range(index - value, index + value + 1):
#                 if index - value >= 0 and index + value in range(len(data)):
#                     data[index] = '0'
#                     data[i] = '0'
#                 else:
#                     print("Strike missed!")
#                     break
#             while '0' in data:
#                 data.remove('0')
#
#         command = input()
#
#     print('|'.join(data))
#
# targets_list = input().split(' ')
# moving_target(targets_list)
