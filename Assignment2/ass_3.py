
def count_vowel(strng):
    if not strng:
        return None
    vowel_lis = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ano_lis = []
    for element in strng:
        if element in vowel_lis and element not in ano_lis:
            print(f"Vowel-{element}, Count-{strng.count(element)}")
            ano_lis.append(element)



count_vowel('Haidar Is a Student')
