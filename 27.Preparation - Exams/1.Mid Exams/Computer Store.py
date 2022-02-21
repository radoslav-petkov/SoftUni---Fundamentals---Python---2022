line = input()

net_price = 0

while line != "special" and line != "regular":
    current_price = float(line)

    if current_price > 0:
        net_price += current_price
    else:
        print("Invalid price!")

    line = input()

if net_price <= 0:
    print("Invalid order!")

else:
    taxes = net_price * 0.2
    final_price = net_price + taxes

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("------------")

    if line == "special":
        final_price = final_price * 0.9

    print(f"Total price: {final_price:.2f}$")




# command = input()
#
# totals = 0
#
# while not (command == "special" or command == "regular"):
#
#     command = float(command)
#     if command <= 0:
#         print("Invalid price!")
#     else:
#         totals += command
#     command = input()
#
# tax = totals * 0.2
# total_price = totals * 1.2
# if total_price == 0:
#     print("Invalid order!")
# if command == "special":
#     total_price = total_price * 0.9
#
# if total_price > 0:
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {totals:.2f}$")
#     print(f"Taxes: {tax:.2f}$")
#     print("-----------")
#     print(f"Total price: {total_price:.2f}$")
