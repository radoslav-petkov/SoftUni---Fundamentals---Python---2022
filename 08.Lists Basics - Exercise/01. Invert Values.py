nums = input().split(' ')
new_list = []

for num in nums:
    if int(num) > 0:
        new_list.append(-int(num))
    else:
        new_list.append(abs(int(num)))
print(new_list)




# orig_list = input().split()
#
# inverted_list = []
#
# for num in orig_list:
#
#     if int(num) > 0:
#         inverted_list.append(int('-' + num))
#
#     elif int(num) < 0:
#         inverted_list.append(abs(int(num)))
#
#     else:
#         inverted_list.append(int(num))
#
# print(inverted_list)


# nums = [-num if num > 0 else abs(num) for num in list(map(int, input ().split(' ')))]
# print(nums)
