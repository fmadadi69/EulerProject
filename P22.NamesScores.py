import string


def names_scores(input_file):

    alphabet = list(string.ascii_uppercase)

    with open(input_file) as names:
        names_list = sorted(names.read().replace('"', '').split(','))

    names_score = 0
    for name_index in range(len(names_list)):
        # print(name_index, [alphabet.index(i) + 1 for i in names_list[name_index]], names_list[name_index])
        names_score += (name_index + 1) * sum(alphabet.index(i) + 1 for i in names_list[name_index])

    return names_score


print(names_scores('./data/names.txt'))
