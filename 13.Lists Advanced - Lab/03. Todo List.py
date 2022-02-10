todo = ["" for i in range(11)]

command = input()

while command != "End":
    explode = command.split("-")
    priority = int(explode[0])
    task = explode[1]
    todo[priority] = task

    command = input()

final_todo = [task for task in todo if task != ""]
print(final_todo)




# todo_list = {}
#
# command_data = input()
# while command_data != 'End':
#     priority, errand, = command_data.split('-')
#     priority = int(priority)
#
#     todo_list[priority] = errand
#
#     command_data = input()
#
# todo_list_sorted = [todo_list[k] for k in sorted(todo_list)]
# print(todo_list_sorted)
