def plusMinus(n,arr):
    # Write your code here
    positive = 0
    negative = 0
    zeros = 0 
    for i in arr:
        if i>0:
            positive+=1
        elif i<0:
            negative+=1
        else:
            zeros+=1
    
    print(positive/n)
    print(negative/n)
    print(zeros/n)

plusMinus(6,[-4,-3,-9,0,4,1])