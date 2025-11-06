def partition(lis):
    low =  0
    high = len(lis) - 1
    mid = (low+high)//2
    pivot = lis[mid]

    left = []
    right = []
    equal = []

    for x in lis:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)
    return left, right, equal

def quick_sort(lis):
    if len(lis) <= 1:
        return lis

    left, right, equal = partition(lis)
    return quick_sort(left) + equal + quick_sort(right)

my_list = [53, 6, 3, 22, 33, 23, 202, 5939, 4, 2, 90]
print(quick_sort(my_list))