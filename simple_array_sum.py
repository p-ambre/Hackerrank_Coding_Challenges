#Given an array of integers, find the sum of its elements.
#For example, if the array , ar = [1,2,3], 1+2+3 = 6, so return 6.

def simpleArraySum(mylist):
    total = 0
    for number in mylist:
        total += number
    print("The sum of the numbers is:", total)

mylist = input('Enter your list: ')
mylist = [int(x) for x in mylist.split()]
simpleArraySum(mylist)
