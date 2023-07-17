import time
collatz_dict = dict()
def collatz_seq(start_num):
    collatz_list = [start_num]

    while collatz_list[-1] != 1:
        if collatz_list[-1] % 2 == 0:
            even_next_item = int(collatz_list[-1]/2)
            if even_next_item in collatz_dict:
                collatz_list+=collatz_dict[even_next_item]
                break
            else:
                collatz_list.append(even_next_item)
        else:
            odd_next_item=collatz_list[-1]*3+1
            if odd_next_item in collatz_dict:
                collatz_list.append(collatz_dict[odd_next_item])
                break
            else:
                collatz_list.append(odd_next_item)

    collatz_dict[start_num]=collatz_list
    return collatz_list

#print(collatz_seq(100))

def longest_collatz_chain(start_num):
    start_time = time.time()
    max_len = (1, 0)
    for i in range(1,start_num+1):
        if len(collatz_seq(i)) >max_len[0]:
            max_len = (len(collatz_seq(i)),i)
    return max_len , f'it has taken {time.time()-start_time} seconds to be solved'

print(longest_collatz_chain(1000000))


