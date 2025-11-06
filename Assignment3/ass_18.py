

def convert(sequence):
    words = sequence.split('-')
    words.sort()
    return '-'.join(words)

# Accept input
user_input = input("Enter hyphen-separated words: ")
result = convert(user_input)
print("Sorted sequence:", result)



def convert(sequence):
    words = []
    word = ""
    for char in sequence:
        if char == '-':
            words.append(word)
            word = ""
        else:
            word += char
    words.append(word)

    for i in range(len(words)):
        min_index = i
        for j in range(i + 1, len(words)):
            if words[j] < words[min_index]:
                min_index = j

        words[i], words[min_index] = words[min_index], words[i]


    result = ""
    for i in range(len(words)):
        result += words[i]
        if i != len(words) - 1:
            result += "-"

    return result


input_sequence = "orange-apple-banana-grape"
print("Sorted sequence:", convert(input_sequence))