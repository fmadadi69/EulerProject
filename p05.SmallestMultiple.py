from collections import defaultdict

def nextprime(num):
    found = False
    next = num+1
    while not found:
        for i in range(2, int((next)**0.5)+1):
            if next % i == 0:
                next=next+1
                break
        else:
            return next


def num_primes(num):
    primes = []
    dict_primes = dict()
    i=2
    while num>1:
        if num % i == 0:
            num = num / i
            primes.append(i)
        else:
            i = nextprime(i)

    for item in set(primes):
        dict_primes[str(item)] = primes.count(item)

    return dict_primes

#print(num_primes(18))


def smallestmultiples(numlist):
    smallest_dict = defaultdict(list)
    dict1 = num_primes(numlist[0])
    mul = 1

    for num in range(1, len(numlist)):
        dict2 = num_primes(numlist[num])

        for key in set().union(dict1, dict2):
            if key in dict1 and key not in dict2:
                smallest_dict[key] = dict1[key]
            elif key not in dict1 and key in dict2:
                smallest_dict[key] = dict2[key]
            elif key in dict1 and key in dict2:
                smallest_dict[key] = max(dict1[key], dict2[key])

        dict1 = smallest_dict

    for key, value in dict1.items():
        mul =mul * int(key)**value


    return smallest_dict, mul


print(smallestmultiples(range(1, 20)))






