arr = [1,2,4,5]

# Cost of operation
# arr[0] # O(1)
# arr.append(7) # O(1)
# arr.pop() # O(1)
# arr.insert(0, 8) # O(n)
# arr.remove(4) # O(n)
# arr.sort() # O(nlogn)
# arr.reverse() # O(n)
# arr.clear() # O(1)
# arr.copy() # O(n)
# arr.count(4) # O(n)
# arr.index(4) # O(n)
# arr.len() # O(1)

# linear scan
# Used in: Finding max/min, Counting, Checking conditions
for x in arr:
    print(x)

# Index based access
# Used when: You need index, Comparing neighbors
for i in range(len(arr)):
    print(arr[i])

# Two pointer approach
# Used when: You need to compare elements from both ends
left = 0
right = len(arr) - 1
while left < right:
    print(arr[left], arr[right])
    left += 1
    right -= 1

# Keep track of answer
# Used when: You need to keep track of the answer as you iterate through the array
max_val = arr[0]
for x in arr:
    if x > max_val:
        max_val = x


#  PROBLEMS
# 1: find maximum value in array without using max()
arr1 = [1,2,3,4,5]
max_num = arr1[0]
for x in arr1:
    if x > max_num:
        max_num = x
print("%n Maximum value without max function", max_num)

# ----------------------------------------------------------------------------
# 2: Count even numbers: how many even numbers in list
arr2 = [2,3,4,5,6]
count = 0
for x in range(len(arr2)):
    if arr2[x] % 2 == 0:
        count+=1
print("%n Count of even numbers", count)

# -------------------------------------------------------------------------
# 3: if array is sorted
arr3 = [1,2,3]
arr4 = [3,2,1]

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print("%n Sorted",is_sorted(arr3))
print("%n Sorted",is_sorted(arr4))

# ------------------------------------------------------------------------
# 4: Second largest elements in arr  without sorting

arr5 = [1,2,4,3,5]
maxi = float('-inf')
second_maxi = float('-inf')

for num in arr5:
    if num > maxi:
        second_maxi = maxi
        maxi = num
    elif num > second_maxi and num!= maxi:
        second_maxi = num

print("%n second largest number", second_maxi)

