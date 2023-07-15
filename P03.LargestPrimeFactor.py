def isprime(num):
    for index in range(2,int(num**0.5)+1):
        if num % index == 0:
            return False
    else:
        return True

def primeFactors(number):
    primeFactorList = []
    for num in range(2,int(number**0.5)+1):
        if number % num == 0 and isprime(num):
                primeFactorList.append(num)

    return primeFactorList

print(primeFactors(13195))
print(primeFactors(600851475143))


