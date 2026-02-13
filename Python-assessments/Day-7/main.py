# 1: First occurrence of the element
# arr = [1,2,2,2,3,4]
# target = 2
# Output → 1
def first_element(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        # When found target → move toward left to find first occurrence.
        mid = (left + right) // 2
        if(arr[mid] == target):
            ans = mid
            right = mid - 1 # move toward left
        elif(arr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return ans

print("First occurrence of element", first_element([1,2,2,2,3,4], 2))
# --------------------------------------------------------------------
# Problem 2: Last Occurrence
# Move right instead of left.
def last_element(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if(arr[mid] == target):
            ans = mid
            left = mid + 1
        elif(arr[mid] < target):
            left = mid + 1
        else: 
            right = mid - 1
    return ans

print("last element", last_element([1,2,2,2,3,4], 2))
# -----------------------------------------------------------------------
# 3: Count the occurrences
def count(arr, target):
    left, right = 0, len(arr) - 1
    first=first_element(arr, target)
    last=last_element(arr, target)

    count = last - first + 1    # when arr is sorted

    return count

print("Count of the elements", count([1,2,2,2,3,4], 2))
# -----------------------------------------------------------------------
# 4: Find Minimum in Rotated Sorted Array
# Input: [4,5,6,7,0,1,2]
# Output: 0
def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
# ------------------------------------------------------------------------
#  5 (Very Important): Binary Search on Answer

# Used when:
# We don’t search element
# We search minimum/maximum possible value
# Condition is monotonic

# Find square root of x. Input: x = 8 and Output: 2
def sq_root(x):
    left, right = 0, x
    ans = 0

    while(left <= right):
        mid = (left + right) // 2
        if mid * mid <= x:
            ans = mid
            left = mid + 1
        else: 
            right = mid - 1
    return ans

print("Square root", sq_root(8))

