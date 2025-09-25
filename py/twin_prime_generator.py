import time
import csv


def user_values():
    while True:
        try:
            upper = int(input("Upper limit: "))
            if upper < 0:
                print("Please enter a value greater than 0!")
            else:
                break
        except ValueError:
            print("Please enter a valid integer!")
    return upper


def write_to_csv(file_name, data):
    with open(f"{file_name}", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["prime"])
        writer.writerows([x] for x in data)
    f.close()


def prime_sieve(limit):
    numbers = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if numbers[p]:
            for i in range(p * p, limit + 1, p):
                numbers[i] = False
        p += 1

    primes = []
    for p in range(2, limit + 1):
        if numbers[p]:
            primes.append(p)
    return primes


def find_twins_in_list(primes):
    twins = []
    for i in range(len(primes) - 1):
        if (primes[i + 1] - primes[i]) == 2:
            twins.append((primes[i], primes[i + 1]))
    return twins


twin_limit = user_values()
start_time = time.time()
primes_list = prime_sieve(twin_limit)
twin_primes = find_twins_in_list(primes_list)
print(twin_primes)
end_time = time.time() - start_time
print(f"Found {len(twin_primes)} twin primes in {end_time:.2f} seconds")

write_to_csv("twin_primes.csv", twin_primes)
