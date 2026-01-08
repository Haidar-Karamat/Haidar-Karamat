
def operation_16():
    lis = []
    for x in range(1, 21):
        tup = tuple([x, x**2, x**3])
        lis.append(tup)
    return lis

print(operation_16())

