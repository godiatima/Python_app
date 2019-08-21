my_foods = ['Pizza', 'Coffee', 'Burger', 'Fish']
friends_food = my_foods[:]

my_foods.append('Cannoli')
friends_food.append('Barbaque')

print("My favorite foods are: ")
for food in my_foods:
	print(my_foods[0] + " is my favorite food" + "\n")

print("\nMy favorite friends food are: ")
print(friends_food)