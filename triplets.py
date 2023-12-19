def compareTriplets(a, b):
    # Write your code here
    bobmark = 0;
    Alicemark = 0;
    
    for i in range(len(a)):
        if a[i]>b[i]:
            Alicemark +=1
        elif a[i]<b[i]:
            bobmark += 1
        else:
            continue
    
    return Alicemark,bobmark
    
result = compareTriplets([1,2,3],[4,5,6])
print(result)