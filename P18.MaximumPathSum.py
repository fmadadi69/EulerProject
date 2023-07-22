triangle_input = ''' 75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# triangle_input = '''3
# 7 4
# 2 4 6
# 8 5 9 3'''
def max_path_sum(triangle_sum):
    triangle_list = [i.strip().split() for i in triangle_input.splitlines()]
    #print(triangle_list)

    row = len(triangle_list)-1
    max_list = [int(i) for i in triangle_list[-1]]
    new_max_list = []

    for i in range(row-1,-1, -1):
        for j in range(len(triangle_list[i])):
            new_max_list.append(int(triangle_list[i][j])+max(max_list[j],max_list[j+1]))
        max_list = new_max_list
        new_max_list = []

    return max_list

print(max_path_sum(triangle_input))








