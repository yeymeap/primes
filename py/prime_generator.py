import csv


def user_values():
    while True:
        try:
            n = int(input("First N primes: "))
            if n < 0:
                print("Please enter a value greater than 0!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer!")
    return n


def write_choice():
    while True:
        value = str(input("Do you want to save decompositions numbers to CSV? (y/n): "))
        if value.lower() == "y":
            return True
        elif value.lower() == "n":
            return False


def write_to_csv(file_name, data):
    with open(f"{file_name}", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["prime"])
        writer.writerows([x] for x in data)
    f.close()


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


def first_n_primes(n):
    primes = []
    count = 0
    i = 2
    while count < n:
        if is_prime(i):
            primes.append(i)
            count += 1
        i += 1
    return primes


n_primes = user_values()
prime_list = first_n_primes(n_primes)
# print(prime_list)

choice = write_choice()
if choice == True:
    write_to_csv("primes.csv", prime_list)
