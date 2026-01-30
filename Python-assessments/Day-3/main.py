# 1: Validd palindrome
str = "madam"

def is_palindrom(str):
    left = 0
    right = len(str) - 1

    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True

print("\n Palindrome", is_palindrom(str))

# -----------------------------------------------------------
# 2: two sum of sorted array
arr = [1,2,3,4,5,6]
target = 6
def sum_is_equals(arr, target):
    left = 0
    right = len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left+1, right+1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return none

print("\n Sum of element", sum_is_equals(arr, target))

# -------------------------------------------------------
# 3: reverse string with extra array
def reverse_str(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

print("\n reverse string", reverse_str(["h","e","l","l","o"]))

# ----------------------------------------------------
# 4: remove duplicated from sorted arr - in place with new length
def remove_duplicates(arr):
    if not arr:
        return 0
    
    write_ptr = 1

    for read_ptr in range(1, len(arr)):
        if arr[read_ptr] != arr[read_ptr - 1]:
            arr[write_ptr] = arr[read_ptr]
            write_ptr += 1
    
    return arr[:write_ptr]   # or return write_ptr

print("remove duplicates", remove_duplicates([1,2,2,3,4,4]))