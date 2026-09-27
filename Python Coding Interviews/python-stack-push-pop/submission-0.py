from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    new_list = []
    length = len(arr) - 1
    count = 0

    while length >= 0 and count < len(arr):
        new_list.append(arr[length])
        count += 1
        length -= 1

    return new_list


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
