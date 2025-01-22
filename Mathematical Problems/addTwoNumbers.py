# l1 -> [2, 3, 1]
# l2 -> [2, 7, 2]
# 132 + 272 -> 404
# def addTwoNumbers(self, l1, l2):
#     revl1 = l1.reverse()
#     revl2 = l2.reverse()
#     sum = []
l1 = [2,4,3] #342
l2 = [5,6,4] #465
l1.reverse()
l2.reverse()
result1 = int("".join(map(str, l1)))
result2 = int("".join(map(str, l2)))
sum = result1 + result2
result = []
for i in str(sum):
    result.append(int(i))
print(result)