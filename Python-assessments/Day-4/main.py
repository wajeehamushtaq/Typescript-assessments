# Problem 1: Maximum Sum Subarray of Size K
# Input: [2,1,5,1,3,2], k = 3
# Output: 9 → [5,1,3]

def max_sum_subarray(arr, k):
    left = 0
    window_sum = 0
    max_sum = 0

    for right in range(len(arr)):
        window_sum += arr[right]
        if max_sum < window_sum:
            max_sum = window_sum
        if right - left + 1 == k:
            window_sum -= arr[left]
            left += 1
            
    return max_sum

print("\n Maxi subarray", max_sum_subarray([2,1,5,1,3,2], 3))
# -------------------------------------------

# Problem 2: Longest Substring Without Repeating Characters
# Input: "abcabcbb"
# Output: 3 → "abc"

def longest_substring(arr):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(arr)):
        while arr[right] in char_set:
            char_set.remove(arr[left])
            left+=1
        char_set.add(arr[right])
        # right - left + 1 gives length of window
        max_len = max(max_len, right - left + 1)
    return max_len

print("\n longest string", longest_substring("abcabcbb"))

# -------------------------------------------------------
# Problem 3: Smallest Subarray with Sum ≥ S

# Input: [2,1,5,2,3,2], S = 7
# Output: 2 → [5,2]
def small_subarr(arr, S):
    left = 0
    window_sum = 0
    min_len = float('inf')

    for right in range(len(arr)):
        window_sum += arr[right]

        while(window_sum >= S):
            window_sum -= arr[left]
            min_len = min(min_len, right - left + 1)
            left += 1
    
    return min_len if min_len != float('inf') else 0


print("\n Smallest subarr", small_subarr([2,1,5,2,3,2], 7))

# --------------------------------------------------------
# Maximum Number of Vowels in a Substring of Length K
# Input: "abciiidef", k = 3
# Output: 3
def max_vowels(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    current_vowels = 0
    max_vowels_count = 0
    left = 0

    for right in range(len(s)):
        if s[right] in vowels:
            current_vowels += 1
        
        if right - left + 1 > k:
            if s[left] in vowels:
                current_vowels -= 1
            left += 1
        max_vowels_count = max(max_vowels_count, current_vowels)
        
    return max_vowels_count

print("Maximum number of vowels",max_vowels("abciiidef", 3))

# Think of this code like a bus with a limited number of seats ($k$) driving through a line of people. 
# Some people are "vowels" and some are not.Here is the "Big Secret": 
# We don't recount everyone on the bus every time. We only care about the person getting on and the person getting kicked off.
# The 3 Simple Rules
# The Person Getting On (right): Every time the bus moves forward, one person gets on. If they are a vowel, your count goes up by 1.
# The Bus is Full (right - left + 1 > k): If the bus only has 3 seats and a 4th person tries to get on, someone must leave from the back (left).
# The Person Getting Off (left): If the person leaving the back seat was a vowel, your count goes down by 1.

# Code Line,What it actually means
# if s[right] in vowels: current += 1,A new vowel just stepped onto the front of the bus.
# if right - left + 1 > k:,"""Hey! The bus is over capacity! Kick someone off the back."""
# if s[left] in vowels: current -= 1,"""Was the person we just kicked off a vowel? If so, subtract them."""
# max_count = max(...),"""What's the most vowels we've had on the bus at one time so far?"""




        
        







