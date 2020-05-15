"""
Given an array of integers, 
find the maximal absolute difference between 
any two of its adjacent elements.

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
"""
def arrayMaximalAdjacentDifference(inputArray):
    maxi = float("-inf")
    for i in range(len(inputArray)-1):
        if abs(inputArray[i+1]-inputArray[i])> maxi:
            maxi = abs(inputArray[i+1]-inputArray[i])
    return maxi

inputArray = [1,5,3,4]
print(arrayMaximalAdjacentDifference(inputArray))