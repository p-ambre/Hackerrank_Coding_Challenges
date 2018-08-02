#Consider a staircase of size :n = 4
#      #
#     ##
#    ###
#   ####
#Observe that its base and height are both equal to , and the image is drawn using
## symbols and spaces. The last line is not preceded by any spaces.
#Write a program that prints a staircase of size n.

def staircase(num_stairs):
    num = num_stairs - 2
    for stairs in range(1, num_stairs):
        print(" " * num, "#" * stairs)
        num -= 1
    print("#" * num_stairs)

num_stairs = int(input())
staircase(num_stairs)
