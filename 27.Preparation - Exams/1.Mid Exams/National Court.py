staff1 = int(input())
staff2 = int(input())
staff3 = int(input())

people = int(input())

time = 0

efficiency = staff1 + staff2 + staff3

while people > 0:

    people -= efficiency
    time += 1

    if time % 4 == 0:
        time += 1

print(f"Time needed: {time}h.")



