#You are in-charge of the cake for your niece's birthday and have decided the
#cake will have one candle for each year of her total age. When she blows out
#the candles, she’ll only be able to blow out the tallest ones. Your task is to
#find out how many candles she can successfully blow out.

#For example, if your niece is turning 4 years old, and the cake will have 4
#candles of height 3, 2, 1, 3, she will be able to blow out 2 candles successfully,
#since the tallest candle is of height 3 and there are 2 such candles.

def birthdayCakeCandles(mylist, n):
    tallest = 0
    count = 0
    for candle in mylist:
        if tallest is None:
            tallest = candle
        if candle > tallest:
            tallest = candle
    for candles in mylist:
        if(tallest == candles):
            count += 1
    return count

n = input()
mylist = [int(x) for x in input().split()]
print(birthdayCakeCandles(mylist, n))

-----------* Method 2 *----------------------

n = input()
arr = [int(x) for x in input().split()]
print(arr.count(max(arr)))
