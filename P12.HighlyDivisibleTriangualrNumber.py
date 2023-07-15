def make_triangular_num(n):
    a = n * (n + 1) / 2
    return int(a)


# print(make_triangular_num(7))

def count_divisibles_of_num(num):
    total = sum(1 for k in range(1, num + 1) if num % k == 0)
    return total




def triangular_divisibles_pair(to_num):
    mydict = {}
    mydict[make_triangular_num(1)] = count_divisibles_of_num(make_triangular_num(1))
    n = 2
    while list(mydict.values())[-1] < to_num:
        mydict[make_triangular_num(n)] = count_divisibles_of_num(make_triangular_num(n))
        n += 1
    return list(mydict.items())[-1]


print(triangular_divisibles_pair(500))
