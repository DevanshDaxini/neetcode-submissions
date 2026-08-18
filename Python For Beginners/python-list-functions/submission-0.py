from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total = 0;
    for val in nums:
        total += val
    
    return total

def get_min(nums: List[int]) -> int:
    small = 999999999

    for val in nums:
        if val < small:
            small = val

    return small

def get_max(nums: List[int]) -> int:
    big = -999999999

    for val in nums:
        if val > big:
            big = val

    return big

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
