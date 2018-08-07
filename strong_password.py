#Louise joined a social networking site to stay in touch with her friends.
#The signup page required her to input a name and a password. However, the
#password must be strong. The website considers a password to be strong if it
#satisfies the following criteria:

#Its length is at least 6.
#It contains at least one digit.
#It contains at least one lowercase English character.
#It contains at least one uppercase English character.
#It contains at least one special character. The special characters are: !@#$%^&*()-+
#She typed a random string of length n in the password field but wasn't
#sure if it was strong. Given the string she typed, can you find the minimum
#number of characters she must add to make her password strong?

def strongPassword(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    count = 0

    if any(i.isdigit() for i in password) == False:
        count += 1
    if any(i.islower() for i in password) == False:
        count += 1
    if any(i.isupper() for i in password) == False:
        count += 1
    if any(i in special_characters for i in password) == False:
        count+=1
    return max(count,6-n)

n = int(input().strip())
password = input().strip()
print(strongPassword(n, password))
