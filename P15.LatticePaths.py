from functools import reduce
def factorial(n):
    return reduce((lambda x,y:x*y),range(1,n+1))

print(factorial(5))

def lattice_path(n,k):
    return (int(factorial(n+k)/factorial(n)/factorial(k)))

print(lattice_path(20,20))