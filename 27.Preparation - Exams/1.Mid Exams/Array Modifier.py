numbers = input().split(" ")
numbers = list(map(int, numbers))

line = input()

while line != "end":
    if line == "decrease":
        numbers = list(map(lambda n: n - 1, numbers))
    else:
        explode = line.split(" ")
        command = explode[0]
        index1 = int(explode[1])
        index2 = int(explode[2])

        if command == "swap":
            numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

        elif command == "multiply":
            numbers[index1] = numbers[index1] * numbers[index2]

    line = input()

numbers = list(map(str, numbers))
output = ", ".join(numbers)

print(numbers)





# numbers = [int(el) for el in input().split()]
# text = input()
#
# while not text == "end":
#
#     if "swap" in text:
#         command, index1, index2 = text.split()
#         index1 = int(index1)
#         index2 = int(index2)
#         numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
#
#     elif "multiply" in text:
#         command, index1, index2 = text.split()
#         index1 = int(index1)
#         index2 = int(index2)
#         numbers[index1] *= numbers[index2]
#
#     elif "decrease" in text:
#         numbers = [num - 1 for num in numbers]
#
#     text = input()
#
# print(*numbers, sep=", ")
