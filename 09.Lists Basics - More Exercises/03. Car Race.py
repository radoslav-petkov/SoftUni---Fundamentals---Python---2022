race = [int(i) for i in input().split(' ')]
finish = len(race) // 2
f_car = race[0:finish]
s_car = race[-1:finish:-1]

score_f_car = 0
score_s_car = 0

for _ in f_car:
    score_f_car += _
    if _ == 0:
        score_f_car *= 0.8

if score_f_car > score_s_car:
    print(f"The winner is right with total time: {score_s_car:.1f}")
else:
    print(f"The winner is left with total time: {score_f_car:.1f}")



# times_list = list(map(int, input().split()))
# center = len(times_list) // 2
# left_time = 0
# right_time = 0
# for left in times_list[:center]:
#     if left == 0:
#         left_time *= 0.8
#     else:
#         left_time += left
# for right in reversed(times_list[center+1:]):
#     if right == 0:
#         right_time *= 0.8
#     else:
#         right_time += right
# time = min([left_time, right_time])
# if left_time == time:
#     winner = 'left'
# else:
#     winner = 'right'
# print(f'The winner is {winner} with total time: {time:.1f}')
