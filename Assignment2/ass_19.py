
def find_position(lis, target_element):
    if not lis:
        return None, None
    try:
        for i in range(len(lis)):
            if lis[i] == target_element:
                print(f"element found {target_element} at index {i}")
        raise ValueError
    except ValueError:
        print(f"{target_element} is not present in list")
        return None, None

my_list = [34, 3, 64, 2, 202, 98, 102]
find_position(my_list, 121)




