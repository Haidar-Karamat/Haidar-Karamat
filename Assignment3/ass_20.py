def frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items()))

text = "cat apple bat car king car"
print(frequency(text))

def frequency(text):
    words = []
    word = ""
    for char in text:
        if char == " ":
            if word:
                words.append(word)
                word = ""
        else:
            word += char
    if word:
        words.append(word)

    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    keys = list(freq.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if keys[i] > keys[j]:
                keys[i], keys[j] = keys[j], keys[i]

    sorted_freq = {}
    for k in keys:
        sorted_freq[k] = freq[k]

    return sorted_freq

text = "cat apple bat car king car"
print(frequency(text))