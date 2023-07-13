def fibo(to_num):
    fibo_list = [1,2]
    i = 2
    while fibo_list[i-1]+fibo_list[i-2]<to_num:
        fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
        i +=1

    return fibo_list

print(fibo(10))

def sum_even_fibo(to_num):
    return sum(item for item in fibo(to_num) if item % 2 ==0)

print(sum_even_fibo(4000000))