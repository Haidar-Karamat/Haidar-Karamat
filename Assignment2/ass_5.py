
def palindrome(strng):
    if strng == strng[::-1]:
        print(f"{strng} is a Palindrome")
    else:
        print(f"{strng} is not Palindrome")


palindrome('madam')