def add_two_numbers() -> int:
    user_input = input()
    
    new_list = user_input.split(",")

    sum = 0

    for x in new_list:
        x = int(x)
        sum += x
    
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
