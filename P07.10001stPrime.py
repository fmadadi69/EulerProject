def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


def next_prime(prime_num):
    next_prime = prime_num + 1
    while not is_prime(next_prime):
        next_prime += 1

    return (next_prime)


def nth_prime(index):
    prime_num = 2
    for i in range(index - 1):
        prime_num = next_prime(prime_num)

    return prime_num


print(nth_prime(10001))