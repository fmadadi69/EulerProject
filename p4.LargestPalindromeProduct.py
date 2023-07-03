def isPalindrome(number):
    strnum = str(number)
    for index in range(int(len(strnum)/2)):
        if strnum[index]!=strnum[-(index+1)]:
            return False
    else:
        return True

print(isPalindrome(102201))

def largestPalindromeProduct(digits):
    num_1 = int(digits*'9')
    num_2 = int(digits*'9')
    maxpal = 0
    for n1 in range(num_1-int((digits-1)*'9')):
        for n2 in range(num_2-int((digits-1)*'9')):
            if isPalindrome((num_1-n1)*(num_2-n2)) and (num_1-n1)*(num_2-n2)> maxpal:
                maxpal = (num_1-n1)*(num_2-n2)
                nn1 = (num_1-n1)
                nn2 = (num_2-n2)
    return maxpal, nn1, nn2


print(largestPalindromeProduct(4))


