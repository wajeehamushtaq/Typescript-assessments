# Problem 1: Range Sum Query

# Input: arr = [1,2,3,4,5], queries = (1,3)
# Output: 2 + 3 + 4 = 9
def range_sum(arr, quer):
    sum = 0
    i = 0
    while(i <= quer[1]):
        if(i >= quer[0] and i <= quer[1]):
            sum += arr[i]
        i+=1
    return sum

print("Range sum query", range_sum([1,2,3,4,5], [1,3]))
# --------------------------------------------------------
# Problem 2: Subarray Sum Equals K

# Input: [1,1,1], k = 2
# Output: 2
# Use prefix sum + hashmap

# prefix_sum = 1
# check → prefix_sum - k = 1 - 2 = -1 ❌ not in map
# map = {0:1, 1:1}

# when prefix_sum = 2
# check → prefix_sum - k = 2 - 2 = 0 ✅ in map
# count += map[0] → count = 1
# map = {0:1, 1:1, 2:1}
def subarray_sum_equals_k(arr, k):
    prefix_sum = 0
    count = 0
    freq = {0: 1}

    for num in arr:
        prefix_sum += num

        if prefix_sum - k in freq:
            count += freq[prefix_sum - k]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count


print("Subarray sum equals", subarray_sum_equals_k([1,1,1], 2))
# -----------------------------------------------------
# Problem 3: Find Total Number of Zero-Sum Subarrays

# Input: [1, -1, 0, 2, -2]
# Output: 4
print("Subarray sum equals", subarray_sum_equals_k([1, -1, 0, 2, -2], 0))

# --------------------------------------------------------
# Problem 4 (Interview): Longest Subarray with Sum K
# Input: [10, 5, 2, 7, 1, 9], k = 15
# Output: 4 → [5,2,7,1]

def longest_subarray_sum_k(arr, k):
    prefix_sum = 0
    max_len = 0
    prefix_map = {}

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # Case 1: subarray from index 0
        if prefix_sum == k:
            max_len = i + 1

        # Case 2: check if (prefix_sum - k) seen before
        if (prefix_sum - k) in prefix_map:
            length = i - prefix_map[prefix_sum - k]
            max_len = max(max_len, length)

        # Store prefix_sum first time only
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_len


print(longest_subarray_sum_k([10,5,2,7,1,9], 15))