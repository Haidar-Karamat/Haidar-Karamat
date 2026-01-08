
def most_freq_word(lis):
    if not lis:
        return None, None

    max_count = 0
    most_freq = None

    for i in range(len(lis)):
        found = False
        for j in range(i):
            if lis[i] == lis[j]:
                found = True
                break

        if not found:
            count = lis.count(lis[i])
            if count > max_count:
                max_count = count
                most_freq = lis[i]
    print(f"Most Frequent Element: {most_freq} → Count: {max_count}")


lis = ['apple', 'cat', 'dog', 'cat']
most_freq_word(lis)