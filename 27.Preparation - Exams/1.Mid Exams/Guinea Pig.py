food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())

for i in range(1, 31):
    food -= 0.300
    if i % 2 == 0:
        hay -= food * 0.05
    if i % 3 == 0:
        cover -= weight / 3

if min(food, hay, cover) > 0.001:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")


# total_food_kg = float(input())
# hay_kg = float(input())
# cover_kg = float(input())
# guinea_weight_kg = float(input())
# month = 30
# day = 1
# food_over = False
#
# total_food_grams = total_food_kg * 1000
# hay_grams = hay_kg * 1000
# cover_grams = cover_kg * 1000
# guinea_grams = guinea_weight_kg * 1000
#
# while day <= month:
#     if day % 1 == 0:
#         total_food_grams -= 300
#         if day % 2 == 0:
#             hay_grams -= total_food_grams * 0.05
#         if day % 3 == 0:
#             cover_grams -= guinea_grams / 3
#     day += 1
#
# if total_food_grams > 0 and cover_grams > 0 and hay_grams > 0:
#     print(
#         f"Everything is fine! Puppy is happy! Food: {(total_food_grams / 1000):.2f}, Hay: {(hay_grams / 1000):.2f}, Cover: {(cover_grams / 1000):.2f}.")
# else:
#     print("Merry must go to the pet store!")