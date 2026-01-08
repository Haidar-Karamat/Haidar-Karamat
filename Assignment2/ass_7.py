

def max_min(num_list):
    if not num_list:
        return None, None
    max_num = num_list[0]
    mini_num = num_list[0]

    for num in num_list:
        if num > max_num:
            max_num = num
        if num < mini_num:
            mini_num = num
    return max_num, mini_num

num_list = [x for x in range(33, 564) if x%2 == 0]

maximum, minimum = max_min(num_list)
print("Max", maximum)
print("Mini", minimum)