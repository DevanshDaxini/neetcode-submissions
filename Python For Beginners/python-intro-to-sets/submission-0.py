from typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:
    new_set = set()
    new_set.add(nums[0])

    temp = nums[0]
    for val in nums:
        if val == temp:
            pass
        else:
            new_set.add(val)
        temp = val

    return new_set

    
# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))
