import time


def is_abundant(num):
    proper_divisors = []
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            proper_divisors.append(i)
    return sum(proper_divisors) > num  # , sum(proper_divisors), sorted(proper_divisors)


# print(is_abundant(24))


def abundant_numbers(to_num):
    abundant_numbers_list = []
    for i in range(1, to_num + 1):
        if is_abundant(i):
            abundant_numbers_list.append(i)

    return abundant_numbers_list


# print(abundant_numbers(100))


def non_abundant_sum(to_num):
    start = time.time()
    nums = abundant_numbers(to_num + 1)
    two_abundant_lists = []
    for i in nums:
        for j in nums:
            if i + j <= to_num:  # and (i+j not in two_abundant_lists):
                two_abundant_lists.append(i + j)

    non_abundant_list = set(range(to_num)).difference(set(two_abundant_lists))

    return len(set(two_abundant_lists)), len(non_abundant_list), sum(non_abundant_list), time.time() - start


print(non_abundant_sum(28123))
