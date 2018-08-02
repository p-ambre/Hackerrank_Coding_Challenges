#Given an array of integers, calculate the fractions of its elements that are
#positive, negative, and are zeros. Print the decimal value of each fraction on
#a new line.

#Testcase:   Input: 6
#                  -4 3 -9 0 4 1
#            Output:0.500000
#                   0.333333
#                   0.166667

def plusMinus(a):
    m = len(a)
    countA = 0
    countB = 0
    countC = 0
    for i in range(0,m):
        if(a[i] > 0):
            countA += 1
        elif(a[i] < 0):
            countB += 1
        else:
            countC += 1
    positives = (countA/m)
    negatives = (countB/m)
    zeros = (countC/m)
    print("{0:.6f}".format(round(positives,7)))
    print("{0:.6f}".format(round(negatives,7)))
    print("{0:.6f}".format(round(zeros,6)))

n = int(input())
a = [int(x) for x in input().split()]
plusMinus(a)
