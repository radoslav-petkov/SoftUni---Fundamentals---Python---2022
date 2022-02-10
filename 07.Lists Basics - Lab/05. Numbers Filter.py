number = int(input())
numbers_list = list()

for i in range(number):
    current = int(input())
    numbers_list.append(current)

filter_word = input()
filtered = list()

for current_number in numbers_list:
    if filter_word == "even":
        if current_number % 2 == 0:
            filtered.append(current_number)

    if filter_word == "odd":
        if current_number % 2 != 0:
            filtered.append(current_number)

    if filter_word == "positive":
        if current_number >= 0:
            filtered.append(current_number)

    if filter_word == "negative":
        if current_number < 0:
            filtered.append(current_number)

print(filtered)




# n = int(input())
#
# evens = []
# odds = []
# negatives = []
# positives = []
#
# for _ in range(n):
#
#     num = int(input())
#
#     if num >= 0:
#         positives.append(num)
#     else:
#         negatives.append(num)
#
#     if num % 2 == 0:
#         evens.append(num)
#     else:
#         odds.append(num)
#
# num_filter = input()


# if num_filter == 'even':
#     print(evens)
# elif num_filter == 'odd':
#     print(odds)
# elif num_filter == 'negative':
#     print(negatives)
# elif num_filter == 'positive':
#     print(positives)


# print(eval(filter_word)) !!!!!!!!!  - може да замести редовете от 57ми до 64ти