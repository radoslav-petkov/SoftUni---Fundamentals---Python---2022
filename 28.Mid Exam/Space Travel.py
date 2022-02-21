travel_route = input().split("||")
starting_fuel = int(input())
starting_ammunition = int(input())
fuel_left = starting_fuel
ammunition_left = starting_ammunition

for i in travel_route:
    command_list = i.split(" ")
    command = command_list[0]
    if len(command_list) == 2:
        data = int(command_list[1])
    if command == "Travel":
        fuel_left -= data
        if fuel_left >= 0:
            print(f"The spaceship travelled {data} light-years.")
        else:
            print("Mission failed.")
            break
    if command == "Enemy":
        if ammunition_left >= data:
            ammunition_left -= data
            print(f"An enemy with {data} armour is defeated.")
        elif ammunition_left < data:
            fuel_left -= 2 * data
            if fuel_left >= 0:
                print(f"An enemy with {data} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    if command == "Repair":
        fuel_left += data
        ammunition_added = 2 * data
        ammunition_left += ammunition_added
        print(f"Ammunitions added: {ammunition_added}.")
        print(f"Fuel added: {data}.")
    if command == "Titan":
        if fuel_left < 0:
            print("Mission failed.")
            break
        else:
            print("You have reached Titan, all passengers are safe.")
