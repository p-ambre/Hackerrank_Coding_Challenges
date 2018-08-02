#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#Input: 3
#11 2 4
#4 5 6
#10 8 -12
#Output: 15

def diagonalDifference(a):
    left_diagonal = 0
    right_diagonal = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(i == j):
                left_diagonal += a[i][j]
                right_diagonal += a[i][len(a[i])-i-1]
    difference = abs(left_diagonal - right_diagonal)
    print(difference)

n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
diagonalDifference(a)
