number = int(input())
search_word = input()
strings = list()

for i in range(number):
    strings.append(input())

print(strings)

filtered = list()

for current_string in strings:
    if search_word in current_string:
        filtered.append(current_string)
print(filtered)




# number = int(input())
# search_word = input()
# strings = list()
# filtered = list()
#
# for i in range(number):
#     current_string = input()
#
#     strings.append(current_string)
#
#     if search_word in current_string:
#         filtered.append(current_string)
#
# print(strings)
# print(filtered)







# n = int(input())
# word = input()
#
# all_strings = []
# matched_strings = []
#
# for _ in range(n):
#
#     string = input()
#
#     all_strings.append(string)
#
#     if word in string:
#         matched_strings.append(string)
#
# print(all_strings)
# print(matched_strings)


#
# n = int(input())
# word = input()
#
# strings = []
# for i in range(n):
#     current_string = input()
#     strings.append(current_string)
# print(strings)
#
# for i in range(len(strings) - 1,-1,-1):
#     if word not in strings[i]:
#         strings.remove(strings[i])
# print(strings)