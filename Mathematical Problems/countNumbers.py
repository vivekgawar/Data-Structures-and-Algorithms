def countDigits(x):
    digits = 0
    while x!=0:
        x //= 10
        digits += 1
    return digits
    
print(countDigits(49))