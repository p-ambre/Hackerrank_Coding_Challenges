#Calculate and print the sum of the elements in an array, keeping in mind
#that some of those integers may be quite large.
#Test with input 1000000001 1000000002 1000000003 1000000004 1000000005

def aVeryBigSum(mylist):
    total = 0
    n = len(mylist)
    for i in range(n):
        total += mylist[i]
    print(total)

mylist = [int(x) for x in input().split()]
aVeryBigSum(mylist)
