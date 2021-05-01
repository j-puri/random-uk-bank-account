import random


def get_random_number_array(size=8):
    array = []
    for x in range(size):
        array.append(random.randint(0, 9))
    return array
