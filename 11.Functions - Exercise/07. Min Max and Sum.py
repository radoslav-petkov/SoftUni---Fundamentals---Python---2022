def min_max_sum_func(nums):
    print(f'The minimum number is {min(nums)}')
    print(f'The maximum number is {max(nums)}')
    print(f'The sum number is: {sum(nums)}')


numbers = list(map(int,input().split(' ')))
min_max_sum_func(numbers)





# input_string = input()
# input_list = [int(x) for x in input_string.split(' ')]
#
# minimum_number = min(input_list)
# maximum_number = max(input_list)
# sum_of_all_numbers = sum(input_list)
#
# print(f"The minimum number is {minimum_number}")
# print(f"The maximum number is {maximum_number}")
# print(f"The sum number is: {sum_of_all_numbers}")
