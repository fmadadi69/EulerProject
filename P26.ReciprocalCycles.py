"""
Mathematics Tips of this problem:
1. The maximum repeating decimals of number n is 'n-1'
2. If number n is prime, its repeating decimal length can be calculated by RECURRING DECIMAL function below
3. If number n is coprime to 10, number n can be written as n=a*b, the length of repeating decimal is equal to the
    LCM of number of repeating decimals of a , b
4. If number n is not coprime to 10, and after prime factorization it can be written as n = 2^a * 5^b * p^c * q^d,
    where p,q are prime numbers and a,b,c,d are the 2,3,p,q, the number of repeating decimal of n is equal to the
    number of repeating decimals p^c * q^d
"""
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


def gcd(n1, n2):
    remainder = 1
    if n1 < n2:
        n1, n2 = n2, n1
    while remainder != 0:
        remainder = n1 % n2
        n1 = n2
        n2 = remainder
    return n1


def lcm(n1, n2):
    return (n1 * n2) / gcd(n1, n2)


primes = prime_nums(1000)

d = {i: 0 for i in range(1, 1000)}
d[3] = 1

for i in primes[3:]:
    d[i] = len(recurring_decimal(i)) # The recurring decimals of prime numbers

for i in range(6, 1000):
    if not d[i]:
        if i % 2 != 0 and i % 5 != 0: # The recurring decimals of numbers which are coprime to 10
            for j in primes:
                if i % j == 0:
                    n1 = d[j] # The recurring decimals of the prime number which is divisor to i
                    n2 = d[i / j] # The recurring decimals of i/j
                    d[i] = int(lcm(n1, n2))
                    break
        else: # The recurring decimals of numbers which are not coprime to 10
            n = i
            while n % 2 == 0:
                n = n / 2
            while n % 5 == 0:
                n = n / 5
            d[i] = d[int(n)]

print(list(d.values()).index(max(d.values())) + 1)

