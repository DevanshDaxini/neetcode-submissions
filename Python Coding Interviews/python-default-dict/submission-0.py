from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    
    word = list(s)

    freq = defaultdict(int)

    for val in word:
        freq[val] += 1
    
    return freq


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    
    # nested list, which means i might need a for loop to traverse through it.
    # skip the first element, that is the key, start at the second element
    # set the range the of the traversal from 1 to len(nums[val])

    # dict that has first num as key and has list as the value of key
    # all numbers associtated to that specifc key get appended to the list in that key val pair

    d = defaultdict(list)

    for row in nums:
        for value in row[1:]:
            d[row[0]].append(value)

    return d




# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
