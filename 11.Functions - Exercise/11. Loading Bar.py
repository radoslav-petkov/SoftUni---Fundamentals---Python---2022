def loading_bar(num):
    if num == 100:
        print('100% Complete!')
        print('[%%%E*] ')
    else:
        percent = (num//10) * '%'
        dots = (10 - (num // 10)) * '.'

        print(f'{num}% [{percent}{dots}]')
        print('Still loading...')



# def loading_bar(n):
#
#     bar = []
#     el_count = n // 10
#
#     for i in range(10):
#         if el_count:
#             bar.append('%')
#             el_count -= 1
#         else:
#             bar.append('.')
#
#     if bar.count('%') == 10:
#         return f"100% Complete!\n[{''.join(bar)}]"
#
#     return f"{n}% [{''.join(bar)}]\nStill loading..."
#
#
# number = int(input())
#
# print(loading_bar(number))
