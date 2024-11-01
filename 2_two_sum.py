# Given an array of integers nums and an integer 
# target, return indices of the two numbers such that they 
# add up to target.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

import math

def twoSumBruteForce(nums, target): 
    # time: O(n2) space: O(1)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return -1

def twoSumDictionary(nums, target):
    # O(n) time, O(n) space
    dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict:
            return [i, dict[complement]]
        dict[nums[i]] = i
    return -1    

def twoSumOnSortedList(nums, target):
    # O(n), O(1)
    L = 0
    R = len(nums) - 1
    while (L<R):
        if nums[L] + nums[R] > target:
            R = R - 1
        elif nums[L] + nums[R] < target:
            L = L + 1
        else:
            return [L,R]
    return -1

 
def twoSumSortedListBinarySearch(nums, target):
    for i in range(len(nums)):
        complement = target - nums[i]
        search = bsearch(nums, complement, i+1, len(nums)-1)
        if search != -1:
            return [i, search]  
    return -1   

def bsearch(arr, searched, start, end):
    L = start
    R = end
    while (L <= R):
        mid = (L+R)//2
        if (searched > arr[mid]):
            L = mid+1
        if (searched < arr[mid]):
            R = mid-1
        if (searched == arr[mid]):
            return mid
    return -1

        
 
 
# TODO binary search on sorted list



    
nums1 = [2,7,11,15]
target1 = 9
# [0,1]



nums2 = [3,2,4]
target2 = 6
# [1,2] 

nums3 = [3,3]
target3 = 6
# [0,1]

result = twoSumSortedListBinarySearch(nums1, target1)
print(result)