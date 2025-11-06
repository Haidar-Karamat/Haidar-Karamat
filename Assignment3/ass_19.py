
def is_palindrome(strng : str) -> str:
    rev_strng = ""
    for char in strng:
        rev_strng = char + rev_strng

    if strng == rev_strng:
        print("String is palindrome ", strng)
    else:
        print("Not palindrome ", strng)

is_palindrome("madamza")
