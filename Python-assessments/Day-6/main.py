# 1. valid parenthesis
def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        else:
            if not stack or stack[-1] != mapping[ch]: # stack[-1] means peak of stack
                return False
            stack.pop()
    return len(stack) == 0
# -----------------------------------------------------
# 2. next greater element
# Input:  [2,1,2,4,3]
# Output: [4,2,4,-1,-1]

# Idea (Monotonic Stack)
# We keep decreasing stack
# When current > stack top → pop & update answer.
def next_element(nums):
    stack = []
    res = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            res[index] = nums[i]
        stack.append(i)
    return res
# ------------------------------------------------------
# 3. remove duplicate characters
# Input: "abbaca"
# Output: "ca"

def remove_dup(s):
    stack = []
    
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)

# -----------------------------------------------------
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
