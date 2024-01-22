import string

show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    # Your code goes here.

    # remove spaces, caps and punct
    adjustedstr = teststr.replace(" ", "").lower().translate(str.maketrans("", "",string.punctuation ))

    # once removed all non letters then reverse the string into another variable
    reversedadjstr = adjustedstr[::-1]

    if reversedadjstr == adjustedstr:
        return True
    else:
        return False
    
print(is_palindrome("Radar"))
print(is_palindrome("Hellow World!"))

def is_palindrome2(teststr):
    # convert the string to all lower case
    temp = teststr.lower()

    # strip all spaces and punctiuation
    newstr = ""

    for c in temp:
        if c.isalnum(): # if the current character in our lower case string is an alpha numeric, add it to the new string
            newstr += c
    
    # get the reverse of the new string that has no spaces or punct
    
    reversestr = ""
    str_index = len(newstr) - 1 # starting at the last index which is the length minus 1

    # until we reach the 0th index of first element of the newstr, add it to the reverse str
    while(str_index >= 0):
        reversestr += newstr[str_index]
        str_index -= 1
    
    if(newstr == reversestr):
        return True
    else:
        return False


print(is_palindrome2("Radar"))
print(is_palindrome2("Hellow World!"))
