def sum_of_the_squares(numlist):
    sum_squares = 0
    for item in numlist:
        sum_squares += item**2
    return sum_squares

def square_of_the_sum(numlist):
    return sum(numlist)**2

def sum_square_diff(nums):
    return square_of_the_sum(nums)-sum_of_the_squares(nums)

print(sum_square_diff(range(1,101)))