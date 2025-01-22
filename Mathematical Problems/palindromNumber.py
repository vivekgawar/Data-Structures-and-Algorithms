def isPalindrome(num):
    temp = num
    rev = 0
    while temp!=0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10
    return rev == num

if __name__ == '__main__':
    print(isPalindrome(52525))