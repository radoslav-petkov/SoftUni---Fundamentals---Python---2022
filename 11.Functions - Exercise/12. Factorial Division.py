def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)


num1 = int(input())
num2 = int(input())
result = factorial(num1) / factorial(num2)
print(f'{result:.2f}')






# def factorial_division(n1, n2):
#
#     f1 = 1
#     f2 = 1
#
#     for i in range(1, n1+1):
#         f1 *= i
#
#     for i in range(1, n2+1):
#         f2 *= i
#
#     if f2 != 0:
#         return f'{f1/f2:.2f}'
#
#
# num1 = int(input())
# num2 = int(input())
#
# print(factorial_division(num1, num2))
