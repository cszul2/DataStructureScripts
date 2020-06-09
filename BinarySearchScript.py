"""
This script was developed to build a binary search algorithm for fun. This script repurposes
what I learned from my university courses on binary searches in C++ and Java.
"""
def binarySearch(array:list, leftIndex:int, rightIndex:int, targetValue:float):
    if rightIndex < leftIndex:
        return -1
    midpointIndex = leftIndex + (rightIndex - leftIndex) // 2
    if array[midpointIndex] == targetValue:
        return midpointIndex
    if array[midpointIndex] < targetValue:
        return binarySearch(array, midpointIndex + 1, rightIndex, targetValue)
    if array[midpointIndex] > targetValue:
        return binarySearch(array, leftIndex, midpointIndex - 1, targetValue)

if __name__ == "__main__":
    testArray = list(range(11))
    testTarget = 6
    result = binarySearch(testArray, 0, len(testArray)-1, testTarget)
    if result == -1:
        print(f"The element {testTarget} could not be found in the array.")
    else:
        print(f"The element {testTarget} is present at index {result}.")
    testTarget = 15
    result = binarySearch(testArray, 0, len(testArray)-1, testTarget)
    if result == -1:
        print(f"The element {testTarget} could not be found in the array.")
    else:
        print(f"The element {testTarget} is present at index {result}.")