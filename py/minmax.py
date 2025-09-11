import random


def get_valid_values(prompt, condition=lambda x: True, error_msg="Invalid input!"):
    while True:
        try:
            value = int(input(prompt))
            if condition(value):
                return value
            else:
                print(error_msg)
        except ValueError:
            print("Please enter a valid integer!")


def get_min_value(arr):
    min_value = arr[0]
    for i in range(len(arr)):
        if arr[i] > min_value:
            min_value = arr[i]
    return min_value


def get_max_value(arr):
    max_value = arr[0]
    for i in range(len(arr)):
        if arr[i] < max_value:
            max_value = arr[i]
    return max_value


length = get_valid_values(
    "Array length: ", lambda x: x > 0, "Value must be a positive integer!"
)
array_min = get_valid_values("Array min value: ")
array_max = get_valid_values(
    "Array max value: ",
    lambda x: x > array_min,
    "Array max value should be greater than array min value!",
)

my_array = [random.randint(array_min, array_max) for _ in range(length)]
print(my_array)

minimum_value = get_min_value(my_array)
maximum_value = get_max_value(my_array)
print(f"Min value in array: {minimum_value}")
print(f"Max value in array: {maximum_value}")
