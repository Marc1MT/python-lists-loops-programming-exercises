#Remember import random function here:
import random

num_random_numbers = 10

random_numbers = []

for _ in range(num_random_numbers):
    random_numbers.append(random.randint(1, 100))

my_list = [4,5,734,43,45]

#The magic is here:

print(my_list + random_numbers)