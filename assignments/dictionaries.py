import random

elements = ["banana", "apple", "orange", "grape", "kiwi"]
fruits = []
fruits_dict = {}

for i in range(50):
    j = random.randint(0, 4)
    fruits.append(elements[j])

for fruit in elements:
    n = fruits.count(fruit)
    fruits_dict[fruit] = n

for key, value in fruits_dict.items():
    print(f"La palabra {key} se repite {value} veces")
