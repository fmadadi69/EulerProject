def collatz_seq(start_num):
    collatz_list = [start_num]

    while collatz_list[-1] != 1:
        if collatz_list[-1] % 2 == 0:
            collatz_list.append(int(collatz_list[-1]/2))
        else:
            collatz_list.append(collatz_list[-1]*3+1)
    else:
        return collatz_list

print(collatz_seq(13))

def longest_collatz_chain(start_num):
    max = (1, 0)
    for i in range(start_num, 1,-1):
        if len(collatz_seq(i))>max[0]:
            max = (len(collatz_seq(i)),i)
    return max

print(longest_collatz_chain(1000000))
