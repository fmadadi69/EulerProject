def fibo(len_limit):
    fibo_list = [0, 1, 1]
    i = 3
    next_item = 2
    while len(str(next_item)) < len_limit:
        fibo_list.append(next_item)
        i += 1
        next_item = fibo_list[i - 1] + fibo_list[i - 2]

    return i


print(fibo(1000))
