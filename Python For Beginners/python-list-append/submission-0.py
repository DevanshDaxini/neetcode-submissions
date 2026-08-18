from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    final_list = my_list

    for val in elements:
        final_list.append(val)

    return final_list


# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
