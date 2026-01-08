
def freq_words(sentence):
    if not sentence.strip():
        return None, None

    words = sentence.split()

    for i in range(len(words)):
        freq = 0
        for j in range(len(words)):
            if words[i] == words[j]:
                freq += 1

        already_counted = False
        for k in range(i):
            if words[i] == words[k]:
                already_counted = True
                break

        if not already_counted:
            print(f"'{words[i]}' occurs {freq} times")

freq_words("this is a very good cat and good kite")
def count_each_element(lis):
    if not lis:
        return None, None

    for i in range(len(lis)):
        freq = 1
        for j in range(len(lis)):
            if i != j and lis[i] == lis[j]:
                freq += 1

        already_counted = False
        for k in range(i):
            if lis[i] == lis[k]:
                already_counted = True
                break

        if not already_counted:
            print(f"{lis[i]} occur in {freq} times")


count_each_element([33, 2, 55, 3, 2, 55, 22, 33])

