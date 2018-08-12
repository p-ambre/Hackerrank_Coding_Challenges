#Sami's spaceship crashed on Mars! She sends a series of SOS messages to Earth
#for help.
#Letters in some of the SOS messages are altered by cosmic radiation during
#transmission. Given the signal received by Earth as a string, s, determine
#how many letters of Sami's SOS have been changed by radiation.

#For example, Earth receives SOSTOT. Sami's original message was SOSSOS.
#Two of the message characters were changed in transit.
#Input: SOSSPSSQSSOR
#Output: 3

def marsExploration(msg, word):
    i = 0
    count = 0
    for i in range(len(msg)):
        if msg[i]!=word[i]:
            count += 1
    print(count)

msg = input()
n = len(msg)
occurences = n/3
word = ("SOS" * int(occurences))
marsExploration(msg, word)
