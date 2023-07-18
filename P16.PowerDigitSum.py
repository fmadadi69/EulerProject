def powre_digit_sum(num, exp):
    power = num ** exp
    return sum(int(i) for i in str(power))

print(powre_digit_sum(2, 1000))