text = input().split(" ")
list = list()
command = text[0]
while command != "end":
    index = 0
    message = text[1]
    if command == "Chat":
        list.append(message)
    elif command == "Delete":
        for word in list:
            if message == word:
                list.remove(message)
    elif command == "Edit":
        edited_version = text[2]
        i = 0
        for word in list:
            if message == word:
                list[i] = edited_version
            i += 1
    elif command == "Pin":
        for i in range(len(list)):
            if message in list:
                list.remove(message)
                list.append(message)
    elif command == "Spam":
        for i in range(1, len(text)):
            message = text[i]
            list.append(message)
    text = input().split(" ")
    command = text[0]

for i in range(len(list)):
    print(list[i])








# chat = []
# while True:
#     input_line = input().split()
#     command = input_line[0]
#     if command == 'end':
#         break
#
#     args = input_line[1:]
#
#     if command == 'Chat':
#         msg = args
#         chat.extend(msg)
#
#     elif command == 'Delete':
#         msg = args[0]
#         if msg in chat:
#             chat.remove(msg)
#
#     elif command == 'Edit':
#         msg, new_msg = args[0], args[1]
#         if msg in chat:
#             chat[chat.index(msg)] = new_msg
#
#     elif command == 'Pin':
#         msg = args[0]
#         if msg in chat:
#             chat.append(chat.pop(chat.index(msg)))
#
#     elif command == 'Spam':
#         chat.extend(args)
#
# print(*chat, sep='\n')