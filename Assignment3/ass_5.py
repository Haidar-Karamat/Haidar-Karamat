def count_name_frequency(names):
    freq = {}
    for name in names:
        name = name.lower()
        if name in freq:
            freq[name] += 1
        else:
            freq[name] = 1
    return freq

names = ["Haidar", "Ubaid", "haidar"]

print(count_name_frequency(names))