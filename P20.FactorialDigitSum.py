def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

#print(factorial(100))

def sum_digits(num):
    return sum(int(i) for i in str(num))


print(sum_digits(factorial(100)))
