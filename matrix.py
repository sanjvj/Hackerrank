def diagonalDifference():
    n = int(input().strip())
    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))
    sum1 = 0
    sum2 = 0
    for i in range(len(a)):
        sum1 += a[i][i]
                
     
    for i in range(len(a)):
        reverse = a[i][len(a)-1-i] 
        sum2 += reverse
    
             
    difference = sum1 - sum2
    if(difference>=0):
        return difference
    else:
        return -difference
    
result = diagonalDifference()
print(result)