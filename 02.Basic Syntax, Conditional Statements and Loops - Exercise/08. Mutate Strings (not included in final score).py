first_word = input()
second_word = input()
for i in range(len(first_word)):
    if first_word[i] != second_word[i]:
        replacement = second_word[i]
        word = first_word[0:i] + replacement + first_word[i + 1:]
        first_word = word
        print(first_word)



# str1 = input()
# str2 = input()
# res = ''
#
# for i in range(len(str1)):
#     if str1[i] == str2[i]:
#         continue
#     res = str2[:i+1] + str1[i+1:]
#     print(res)
#
#
#
# # first_string = input()
# # second_string = input()
# # final_string = first_string
# # for char in range(len(first_string)):
# #     final_string = ""
# #     if first_string[char] != second_string[char]:
# #         final_string = second_string[:char+1] + first_string[char+1:]
# #         print(final_string)
# #
# #
# #
# #
# # str1 = input()
# # str2 = input()
# #
# # current_str = ''
# # prev_str = str1
# #
# # for idx in range(len(str1)):
# #     current_str = str2[0:idx+1]+str1[idx+1:]
# #     if not current_str == prev_str:
# #         print(current_str)
# #     prev_str = current_str
# #     current_str = ''
#


# text_1 = input()
# text_2 = input()
# text = text_1
#
# for x in range(len(text_1)):
#     s1 = text_1[x + 1: len(text_1)]
#     s2 = text_2[0:x + 1]
#     if s2 + s1 == text:
#         continue
#     text = s2 + s1
#     print(text)
