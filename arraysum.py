
def simpleArraySum():
    sum = 0
    n = int(input())
    
    input_string = input()
    arr = [];
    current = ""
    for x in input_string:
        if x!=' ':
            current += x
        else:
            arr.append(current)
            current = ""
    arr.append(current)
    
    
    arr = [int(j) for j in arr]
    for i in range(n):
        sum+=arr[i]
    return sum
result = simpleArraySum()
print(result)
