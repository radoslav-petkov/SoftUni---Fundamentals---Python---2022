budget = float(input())
initial_capital = float(input())
number_of_investors = int(input())

collected_money = initial_capital

for index in range(1, number_of_investors+1):
    money = float(input())
    print(f'Investor {index} gave us {money:.2f}.')

    collected_money += money

    if collected_money >= budget:
        extra_money = collected_money - budget
        print(f'We will manage to build it. Start now! Extra money - {extra_money:.2f}.')
        break

if not collected_money >= budget:
    difference = budget - collected_money
    print(f'Project can not start. We need {difference:.2f} more.')