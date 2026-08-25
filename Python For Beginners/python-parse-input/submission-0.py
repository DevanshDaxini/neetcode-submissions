from typing import List

def read_integers() -> List[int]:
    user_input = input()
    
    new_list = user_input.split(",")

    return [int(x) for x in new_list]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
