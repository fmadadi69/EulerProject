import numpy as np
def make_triangular_num(n):
    a = n * (n + 1) / 2
    return int(a)


# print(make_triangular_num(7))

# def count_divisibles_of_num(num):

def isprime(num):
    for i in range(2, int(num ** 2) + 1):
        if num % i == 0:
            return False
    else:
        return True


def nextprime(num):
    num += 1
    while isprime(num):
        num += 1
    return num


def prime_factors(num):
    primeFactors = []
    prime_factors_dict = dict()
    i = 2
    while (num > 1):
        if num % i == 0:
            primeFactors.append(i)
            num = num / i
        else:
            i = nextprime(i)
    for item in set(primeFactors):
        prime_factors_dict[item] = primeFactors.count(item)

    return prime_factors_dict


print(prime_factors(28).values())
print(np.prod([i+1 for i in list(prime_factors(28).values())]))


def triangular_divisibles_pair(to_num):
    mydict = {}
    mydict[make_triangular_num(1)] =np.prod([i+1 for i in prime_factors(1).values()])
    n = 2
    while list(mydict.values())[-1] < to_num:
        mydict[make_triangular_num(n)] =np.prod([i+1 for i in prime_factors(make_triangular_num(n)).values()])
        n += 1
    return list(mydict.items())[-1]


print(triangular_divisibles_pair(500))
