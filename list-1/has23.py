"""
Given an int array length 2, return True if it contains a 2 or a 3.

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""

def has23(nums):
    for ele in nums:
        if 2 in nums or 3 in nums:
            return True
        else:
            return False
        
print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))