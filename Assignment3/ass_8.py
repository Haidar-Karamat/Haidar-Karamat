def group_by_starting_char(words):
    grouped = {}
    for word in words:
        key = word[0]
        if key in grouped:
            grouped[key].append(word)
        else:
            grouped[key] = [word]
    return grouped

words = ['app', 'ant', 'ash', 'bat', 'brand', 'cow', 'cold', 'cot']

print(group_by_starting_char(words))