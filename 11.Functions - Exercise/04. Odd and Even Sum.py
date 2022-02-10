def odd_even_sum(nums):
    odd_sum = 0
    even_sum = 0
    for num in nums:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    print(f'0dd sum = {odd_sum}, Even sum = {even_sum}')


numbers = map(int, list(input()))
odd_even_sum(numbers)






# def odd_and_even_sum(num):
#     odd_list = []
#     even_list = []
#
#     for d in str(num):
#         odd_list = [int(d) for d in str(num) if int(d) % 2 != 0]
#         even_list = [int(d) for d in str(num) if int(d) % 2 == 0]
#
#     return f'Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}'
#
#
# number = int(input())
#
# print(odd_and_even_sum(number))
