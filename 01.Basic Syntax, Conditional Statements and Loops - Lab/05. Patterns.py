number = int(input())

for i in range(number):
    for j in range(0, i+1):
        print("*", end="")
    print()

for i in range(number-1):
    for j in range(number, i, -1):
        print("*", end="")
    print()



# number = int(input())
#
# for i in range (number):
#     for j in range (0, i + 1):
#         print ("*", end="")
#     print()
# for i in range(number-1, 0, -1):
#     for j in range (0, i):
#         print("*", end="")
#     print()



# num = int(input())
#
# for i in range(1, num):
#     print(i * "*")
# for i in range(num):
#     print((num - i) * "*")
