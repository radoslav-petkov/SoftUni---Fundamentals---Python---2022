person_1 = int(input())
person_2 = int(input())
person_3 = int(input())
capacity = person_1 + person_2 + person_3
students = int(input())

hour = 0

while students > 0:
    students -= capacity
    hour += 1

    if hour % 4 == 0:
        hour += 1

print(f"Time needed: {hour}h.")



# first_employee = int(input())
# second_employee = int(input())
# third_employee = int(input())
# number_of_students = int(input())
#
# hours = 0
#
# students_per_hour = first_employee + second_employee + third_employee
#
# while number_of_students > 0:
#     hours += 1
#     if hours % 4 != 0:
#         number_of_students -= students_per_hour
#     if hours % 4 == 0:
#         pass
#
#
# print(f"Time needed: {hours}h.")
