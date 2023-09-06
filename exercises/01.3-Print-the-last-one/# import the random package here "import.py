
original_command = '/usr/local/bin/python "/workspaces/python-lists-loops-programming-exercises/exercises/01.3-Print-the-last-one/# import the random package here "import.py"'
corrected_command = $(echo "$original_command" | sed 's/#.*import.py/import.py/')
echo "$corrected_command"

import random

def generate_random_list():
    aux_list = []
    randonlength = random.randint(1, 100)

    for i in range (randonlength):
        aux_list.append(randonlength)
        i += i
    return aux_list
my_stupid_list = generate_random_list()

