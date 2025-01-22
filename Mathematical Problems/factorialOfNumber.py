def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = n
        while n > 1:
            result *= n-1
            n -= 1 
        return result
print(factorial(4))