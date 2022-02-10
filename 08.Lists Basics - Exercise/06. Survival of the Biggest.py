nums = input().split(' ')
copy_nums = list(map(int, nums))
count = int(input())

for _ in range(count):
    current_min_element = min(copy_nums)
    nums.remove(str(current_min_element))
    copy_nums.remove(current_min_element)

print(', '.join(nums))





# numbers_list = input().split()
# n = int(input())
#
# for i in range (len (numbers_list)):
#     numbers_list[i] = int(numbers_list[i])
#
# for i in range (n):
#     min_element = min(numbers_list)
#     numbers_list.remove (min_element)
#
# for i in range (len (numbers_list)):
#     numbers_list[i] = str(numbers_list[i])
#
# print(', '.join(numbers_list))
    