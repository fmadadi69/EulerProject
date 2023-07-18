def num_to_word(num):
    one_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    one_digits_dict = dict(zip(range(10), one_digits))

    two_digits = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                  'nineteen']
    two_digits_dict = dict(zip(range(10, 20), two_digits))

    two_digits_second = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    two_digits_second_dict = dict(zip([20, 30, 40, 50, 60, 70, 80, 90], two_digits_second))

    num_count = len(str(num))
    num_dict = dict((10**(num_count-i-1) , str(num)[i]) for i in range(num_count))

    word = ''
    under_twenty = False
    for i, j in  num_dict.items():
        if len(str(i)) == 4:
            word += f'{one_digits_dict[int(j)]} thousand and'
            other_values = list(num_dict.values())
            other_values.remove(j)
            if all(int(k)==0 for k in other_values):
                word = word.replace(' and', '')
        elif len(str(i)) == 3 and int(j)==0:
            continue
        elif len(str(i)) == 3:
            word += f' {one_digits_dict[int(j)]} hundred and'
            other_values = list(num_dict.values())
            other_values.remove(j)
            if all(int(k)==0 for k in other_values):
                word = word.replace(' and', '')
        elif len(str(i)) == 2 and int(j)==0:
            continue
        elif len(str(i)) == 2 and int(j) in range(2,10):
            word += f' {two_digits_second_dict[int(j+"0")]}'
        elif len(str(i)) == 2 and int(j) ==1:
            under_twenty = True
        elif len(str(i)) == 1 and under_twenty:
            new_j = int('1'+j)
            word += f' {two_digits_dict[new_j]}'
        elif len(str(i)) == 1 and int(j)==0 and len(list(num_dict.values()))>1:
            continue
        else:
            word += f' {one_digits_dict[int(j)]}'

    return word


def count_num_word(num):
    word = num_to_word(num).replace(' ', '')
    return len(word)

def count_range_of_nums_words(start , end):
    letter_counts = 0
    for i in range(start, end+1):
        letter_counts+=count_num_word(i)
        #print(num_to_word(i))

    return letter_counts


print(count_range_of_nums_words(1,1000))

