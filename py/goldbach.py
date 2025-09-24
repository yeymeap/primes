def user_values():
    while True:
        try:
            decomposition = int(input("Number for decomposition: "))
            if decomposition <= 5:
                print("Please enter a value greater than 5!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer!")
    return decomposition


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


def decomposition_numbers(n):
    decomps_list = []
    if n % 2 == 0:  # even numbers
        for p1 in range(2, n // 2 + 1):
            p2 = n - p1
            if (is_prime(p1) and is_prime(p2)) == True:
                decomp = f"{p1} + {p2} = {n}"
                decomps_list.append(decomp)
                print(decomp)
    elif n > 5:  # odd numbers
        for p1 in range(2, n):
            if not is_prime(p1):
                continue
            for p2 in range(p1, n):
                if not is_prime(p2):
                    continue
                p3 = n - p1 - p2
                if p3 >= p2 and is_prime(p3):
                    decomp = f"{p1} + {p2} + {p3} = {n}"
                    decomps_list.append(decomp)
                    print(decomp)
    return decomps_list


def write_choice():
    while True:
        value = str(input("Do you want to save decompositions numbers to TXT? (y/n): "))
        if value.lower() == "y":
            return True
        elif value.lower() == "n":
            return False


def write_to_txt(file_name, text):
    with open(f"{file_name}", "w") as f:
        for items in text:
            f.write("%s\n" % items)
    f.close()


decomposition = user_values()
decomposition_list = decomposition_numbers(decomposition)

choice = write_choice()
if choice == True:
    write_to_txt("goldbach.txt", decomposition_list)
