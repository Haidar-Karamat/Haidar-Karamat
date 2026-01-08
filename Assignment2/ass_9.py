
def freq_each_ele(lis):
    if not lis:
        return None, None

    for i in range(len(lis)):
        found = False
        for j in range(i):
            if lis[i] == lis[j]:
                found = True
                break

        if not found:
            print(f"Element {lis[i]}\nCount {lis.count(lis[i])}")


lis = [101, 34, 3, 2, 55, 3, 2, 589, 2, 1, 3, 1]
freq_each_ele(lis)