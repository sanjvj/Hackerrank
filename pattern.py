def staircase(n):
    # Write your code here
    for i in range(n):
        for j in range(i, n-1):
            print(" ", end="")
        for j in range(i + 1):
            print("#", end="")
        print()
staircase(5)