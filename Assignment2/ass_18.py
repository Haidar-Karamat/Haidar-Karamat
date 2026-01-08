def count_element(tup, target):
    if not tup:
        return None, None

    for i in range(len(tup)):
        if tup[i] == target:
            print(f"element {target}\nfrequency {tup.count(target)}")
            return target, tup.count(target)
    print(f"{target} is not found in tuple")
    return None, None

tup = (23, 5, 33, 5, 89, 3, 5)
count_element(tup, 23)
