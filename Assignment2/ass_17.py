def unpack_tuple(*args):
    print("Tuple unpacked into individual elements:")
    for i, val in enumerate(args):
        print(f"Element {i}: {val}")


tup1 = (10, 20, 30)
tup2 = (1, 2, 3, 4, 5, 6, 7)
tup3 = ("apple", "banana", "cherry", "date")


unpack_tuple(*tup1)
unpack_tuple(*tup2)
unpack_tuple(*tup3)