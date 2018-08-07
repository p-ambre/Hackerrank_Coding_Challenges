#Alice wrote a sequence of words in CamelCase as a string of letters, s,
#having the following properties:

#It is a concatenation of one or more words consisting of English letters.
#All letters in the first word are lowercase.
#For each of the subsequent words, the first letter is uppercase and rest of the
#letters are lowercase.
#Given s, print the number of words in s on a new line.

#For example,s = oneTwoThree. There are 3 words in the string.

def camelCase(wordlist):
    count = 0
    for letters in wordlist:
        if ord(letters) >= 65 and ord(letters) <= 90:
            count += 1
    count += 1
    return count

word = input()
wordlist = list(word)
print(camelCase(wordlist))
