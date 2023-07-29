# First Solution #################################################
from itertools import permutations


def lexicographic_permutation(per_num):
    return list(permutations(range(0, 10)))[per_num]


print(lexicographic_permutation(999999))

# Second Solution #################################################

permutation_list = []


def tostring(alist):
    return ''.join(alist)


def permute(input_list, index, input_len):
    if index == input_len:
        permutation_list.append(tostring(input_list))
    else:
        for i in range(index, input_len):
            input_list[i], input_list[index] = input_list[index], input_list[i]
            permute(input_list, index + 1, input_len)
            input_list[i], input_list[index] = input_list[index], input_list[i]


mylist = [str(i) for i in list(range(0, 10))]
permute(mylist, 0, len(mylist))
print(sorted(permutation_list)[999999])
