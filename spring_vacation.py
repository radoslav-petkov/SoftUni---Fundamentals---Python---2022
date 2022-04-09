days = int(input())
budget = float(input())
people = int(input())
fuel_km = float(input())
food = float(input())
room = float(input())
fail = False
food_cost = days * people * food
accommodation = days * people * room
if people > 10:
    accommodation *= 0.75
total = food_cost + accommodation

for n in range(1, days + 1):
    km = float(input())
    travel = km * fuel_km
    total += travel
    if round(total, 2) > budget:
        fail = True
        break
    if n % 3 == 0:
        total *= 1.4
    if n % 5 == 0:
        total *= 1.4
    if n % 7 == 0:
        receive = total / people
        total -= receive
    if round(total, 2) > budget:
        fail = True
        break

if fail:
    print(f'Not enough money to continue the trip. '
          f'You need {total - budget:.2f}$ more.')
else:
    print(f'You have reached the destination. '
          f'You have {abs(total - budget):.2f}$ budget left.')
