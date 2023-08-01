def recurring_decimal(divisor):
    if divisor < 10:
        divident = 10
    elif 10 <= divisor < 100:
        divident = 100
    elif divisor < 1000:
        divident = 1000
    else:
        return 'divisor should be less than 10.'
    value_to_check = divident
    recurring_seg = ''
    for i in range(divisor):  # !!! The maximum length of recurrence sequence of number N is N-1 !!!
        recurring_seg += str(divident // divisor)
        divident = divident % divisor
        if divident < divisor:
            divident = divident * 10
            if divident < divisor:
                divident = divident * 10
                recurring_seg += '0'
                if divident < divisor:
                    divident = divident * 10
                    recurring_seg += '0'
        if divident == value_to_check:
            return recurring_seg


#print(recurring_decimal(3))


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


def next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    else:
        return num


def prime_nums(to_num):
    prime_list = [2]
    next_item = next_prime(prime_list[-1])
    while next_item <= to_num:
        prime_list.append(next_item)
        next_item = next_prime(prime_list[-1])

    return prime_list


print(prime_nums(100))


def gcd(n1, n2):
    remainder = 1
    if n1 < n2:
        n1, n2 = n2, n1
    while remainder != 0:
        remainder = n1 % n2
        n1 = n2
        n2 = remainder
    return n1


#print(gcd(18, 36))


def lcm(n1, n2):
    return n1 * n2 / gcd(n1, n2)


primes = prime_nums(1000)
d = {i: 0 for i in range(1, 1000)}
print(primes[0])

d[3] = 1
for i in primes[3:]:
    d[i] = len(recurring_decimal(i))

for i in range(6, 1000):
    if not d[i]:
        if i % 2 != 0 and i % 5 != 0:
            for j in primes:
                if i % j == 0:
                    n1 = j
                    n2 = i / j
                    d[i] = int(lcm(n1, n2))
                    break
        else:
            n = i
            while n % 2 == 0:
                n = n / 2
            while n % 5 == 0:
                n = n / 5
            d[i] = d[int(n)]

#print(list(d.values()).index(max(d.values())) + 1)


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
        if is_prime1[i] == True:
            prime.append(i)
    return prime

print(sieve(100))
