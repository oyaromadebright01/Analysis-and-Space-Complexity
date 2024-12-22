# O(log n) = logarithm time complexity
# recursive function = a fn that calls itself inside the function

import time


def test(n):
    if (n <= 1):
        return
    print("coding")
    test(n/2)

test(9)

import math
print(math.log(8, 2))



# space complexity => space/memory required to complete an algorithm
# TYpes of space complexity
# 1. Auxiliary Space is referred to as Space Complexity in several areas. 
# 2. Auxiliary Space: The extra space or temporary space used by an algorithm.
# 3. The overall space with the input size is known as its space complexity. 
# 4. Space complexity includes both Auxiliary space and space used by input.

# O(1)
def sum(n):
    return n * (n+1)/2
    # space complexity O(1), auxilary)(1)
# O(n)
def arraySum(a):
    sum=0
    for i in a:
        sum += i
    return sum
    # space complexity O(n), auxiliary O(1)




# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
