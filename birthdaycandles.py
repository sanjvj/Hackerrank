def birthdayCakeCandles(n,candles):
    # Write your code here
    candles = sorted(candles)
    count = 0;
    for i in candles:
        if i==candles[-1]:
            count+=1
    
    return count

print(birthdayCakeCandles(4,[3,2,1,3]))