def sum_proper_divisors(num):
    proper_divisors = []
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            proper_divisors.append(i)
    return sum(proper_divisors)


#print(sum_proper_divisors(220))


def is_amicable(num):
    if sum_proper_divisors(sum_proper_divisors(num)) == num and num != sum_proper_divisors(num):
        return  num, sum_proper_divisors(num)

#print(is_amicable(284))

def sum_all_amicables(to_num):
    all_nums = [i for i in range(2, to_num)]
    amicable_nums = []
    for i in all_nums:
        if is_amicable(i):
            amicable_nums.extend(is_amicable(i))
            all_nums.remove(is_amicable(i)[1])
    return sum(amicable_nums), amicable_nums


print(sum_all_amicables(10000))

