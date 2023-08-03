# Solution number 1 #####################################
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

# Solution number 2 #####################################
def sieve(n):
    is_prime1 = [True] * n
    is_prime1[0] = False
    is_prime1[1] = False
    for i in range(2, int(n ** 0.5 + 1)):
        index = i * 2
        while index < n:
            is_prime1[index] = False
            index = index + i
    prime = []
    for i in range(n):
        if is_prime1[i]:
            prime.append(i)
    return prime

print(sieve(1001)[-1])