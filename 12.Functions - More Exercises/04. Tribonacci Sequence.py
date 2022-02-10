number = int(input())

tribonacci_sequence = [0] * number
tribonacci_sequence[0] = 1

for index in range(1, len(tribonacci_sequence)):
    if index < 4:
        tribonacci_sequence[index] = sum(tribonacci_sequence)
    else:
        tribonacci_sequence[index] = sum(tribonacci_sequence[index - 3:index])

print(*tribonacci_sequence)




# def tribonacci(start, num):
#     if num >= 3:
#         for _ in range(num - 1):
#             num = sum(start[-3:])
#             start.append(num)
#         return start
#     else:
#         for _ in range(num - 1):
#             num = sum(start[-2:])
#             start.append(num)
#         return start
#
#
# start = [1]
# number = int(input())
# print(*tribonacci(start, number))