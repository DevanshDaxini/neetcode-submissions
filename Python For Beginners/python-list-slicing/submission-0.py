from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    new_list = []
    count = 0

    for val in my_list[::-1]:
        if count == 3:
            break
        count += 1
        new_list.append(val)
    
    flip_list = []

    for val in new_list[::-1]:
        flip_list.append(val)

    return flip_list


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
