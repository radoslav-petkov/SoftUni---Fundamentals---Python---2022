base_list = input().split(" ")
final_list = list()

for n in base_list:
    final_n = round(float(n))
    final_list.append(final_n)

print(final_list)




# def convert_list_to_round(base_list):
#     final_list = list()
#     for n in base_list:
#         final_n = round(float(n))
#         final_list.append(final_n)
#     return final_list
#
# input_list = input().split(" ")
# print(convert_list_to_round(input_list))
