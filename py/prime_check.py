def user_values():
    while True:
        try:
            number = int(input("Number to check for prime: "))
            if number < 1:
                print("Please enter a value greater than 0!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer!")
    return number


def is_prime(n):  # checks if input number is prime based on 6k +- 1 formula
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:  # checks up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


number = user_values()
prime = is_prime(number)

if prime == True:
    print(f"The number {number} is prime!")
else:
    print(f"The number {number} is not prime!")
