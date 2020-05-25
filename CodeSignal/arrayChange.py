"""
You are given an array of integers. 
On each move you are allowed to increase 
exactly one of its element by one. 
Find the minimal number of moves required 
to obtain a strictly increasing sequence from the input.

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.

"""

def arrayChange(inputArray):
    # initialize pointer 
    i = 0
    # intialize moves
    moves = 0
    # go throught all the array until one position before end 
    while i < len(inputArray)-1:
        # if the next position is smaller or equal to the current position
        if inputArray[i] >= inputArray[i+1]:
            # save the actual value of the next position
            pivot = inputArray[i+1]
            # make the next position equal to bigger by one of the actual position
            inputArray[i+1] = inputArray[i]+1
            # calculate all moves 
            moves += inputArray[i+1] - pivot 
        i += 1
    return moves

inputArray = [1, 1, 1]
print(arrayChange(inputArray))