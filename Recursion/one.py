def printNumbers(Lrange,Rrange):
    # Base case: if Lrange is greater than Rrange, return
    if Lrange > Rrange:
        return
    print(Lrange)  # Print the current number
    # Recursive call with the next number
    printNumbers(Lrange + 1, Rrange)

# Example usage
Lrange = 1
Rrange = 5
printNumbers(Lrange, Rrange)