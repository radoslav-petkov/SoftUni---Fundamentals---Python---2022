names = input(). split(", ")

sorted_names = sorted(names)
sorted_names = sorted(sorted_names, key = lambda name: -len(name))

print(sorted_names)



# name_list = [x for x in input().split(', ')]
# sorted_list = sorted(name_list, key=lambda x: (-len(x), x))
# print(sorted_list)