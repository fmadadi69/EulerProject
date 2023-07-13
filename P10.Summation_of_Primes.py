def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i ==0:
            return False
    else:
        return True


print(is_prime(10037))

def sum_primes(to_num):
    return sum(i for i in range(2, to_num) if is_prime(i))


print(sum_primes(2000000))