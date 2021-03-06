"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges,
awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet a = (a[0],a[1],a[2]), and the rating for
Bob's challenge to be the triplet b = (b[0],b[1],b[2]).

Your task is to find their comparison points by comparing a[0] with b[0],a[1] with b[1], and a[2] with b[2].

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] == b[i], then neither person receives a point.
Comparison points is the total points a person earned.
Sample input 1: 5 6 7
                3 6 10
Output: 1 1
Sample input 2: 17 28 30
                99 16 8
Output: 2 1
"""

def compareTriplets(a,b):
    i = 0
    n = len(a)
    countA = 0
    countB = 0
    for i in range (n):
        if a[i] > b[i]:
            countA += 1
        elif a[i] < b[i]:
            countB += 1
        else:
            pass
    print(countA,countB)

a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
compareTriplets(a,b)
