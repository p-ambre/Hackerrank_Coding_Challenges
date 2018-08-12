"""
Roy wanted to increase his typing speed for programming contests. His
friend suggested that he type the sentence "The quick brown fox jumps over the
lazy dog" repeatedly. This sentence is known as a pangram because it contains
every letter of the alphabet.

After typing the sentence several times, Roy became bored with it so he started
to look for other pangrams.

Given a sentence, determine whether it is a pangram. Ignore case.
"""

def checkPangram(inp_string):
    check_lst = []
    for i in range(26):
        check_lst.append(False)
    for letter in inp_string.lower():
        if not letter == " ":
            check_lst[ord(letter) - ord('a')] = True
    for value in check_lst:
        if value == False:
            return False
    return True

inp_string = input()
if (checkPangram(inp_string) == True):
    print("pangram")
else:
    print("not pangram")
