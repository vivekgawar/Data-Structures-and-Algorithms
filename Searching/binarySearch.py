# Divides the list in two parts lhs and rhs, increments and decrements according to the value's index required
list1 = [1, 2, 4, 5, 7, 8]
def bSearch(l, x):
    high = len(l)-1 #last index of list
    low = 0
    while low <= high: #to exit the loop when the value is not in the array 
        mid = (high + low) // 2
        if x == l[mid]:
            return mid 
        elif x > l[mid]:
            low = mid + 1 #if the 'x' value is bigger than the middle element of array then we set a new 'low'
        else:
            high = mid - 1 #if the 'x' value is smaller than the middle element of array then we set a new 'high'

    return -1
print(bSearch(list1, 5)) #output --> 3 