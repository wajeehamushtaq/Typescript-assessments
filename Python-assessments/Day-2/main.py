# Count frequency of each characters in string
# Use Hash maps or dictionary
s = "hello world"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
# print(freq)

# Time and space O(n)

# Pythonic version CORE PATTERN
# If you know this → 50% string problems solved
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1 

# print(freq)

# ---------------------------------------------------------
# 2: Valid anagram: same length and frequency
def is_anagram(str1, str2):
    freq1 = {}
    freq2 = {}
    if(len(str1) == len(str2)):
        for ch in str1:
            freq1[ch] = freq1.get(ch, 0) + 1
        for ch in str2:
            freq2[ch] = freq2.get(ch, 0) + 1
        return freq1 == freq2
    else:
        return False

# def is_anagram(str1, str2):
#     if len(str1) != len(str2):
#         return False

#     freq = {}
#     for ch in str1:
#         freq[ch] = freq.get(ch, 0) + 1

#     for ch in str2:
#         if ch not in freq or freq[ch] == 0:
#             return False
#         freq[ch] -= 1

#     return True

print("is anagram", is_anagram("listen", "silent"))

# ------------------------------------------------------------
# 3: First non repeating characters: count freq and loop again and find freq 1
str = "swiss"

def first_non_repeat_char(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return None

print("first non repeating number", first_non_repeat_num(str))

# --------------------------------------------------------------
# 4: are all characters unique
str1 = "abcde"
str2 = "aabb"

def is_unique(str):
    freq = {}
    for ch in str:
        freq[ch] = freq.get(ch, 0) + 1
    for x in freq.values():
        if x != 1:
            return False
    return True

print('is unique characters', is_unique(str2))