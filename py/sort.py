import random
import math
import time


def user_values():
    while True:
        try:
            size = int(input("Array size: "))
            if size <= 0:
                print("Please enter a value greater than 0!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer!")
    while True:
        try:
            lower = int(input("Random number lower limit: "))
            if math.isnan(lower):
                print("Please enter a valid integer!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer!")
    while True:
        try:
            upper = int(input("Random number upper limit: "))
            if math.isnan(upper):
                print("Please enter a valid integer!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer!")
    return size, lower, upper


def random_array(array_size, lower_limit, upper_limit):
    arr = [random.randint(lower_limit, upper_limit) for _ in range(array_size)]
    return arr
