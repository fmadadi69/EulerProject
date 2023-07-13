def mul_3(to_num):
    return [i for i in range(3,to_num,3) if i%3 ==0]
def mul_5(to_num):
    return [i for i in range(5,to_num,5) if i%5 ==0]

def sum_mul_3_5(to_num):
    return sum(set(mul_3(to_num)+ mul_5(to_num)))

print(mul_3(1000), mul_5(1000))
print(sum_mul_3_5(1000))