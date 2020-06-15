def almostIncreasingSequence(sequence):

    def helper(newArray):
        # print(newArray)
        if len(newArray)<2:
            return True
        for i in range(len(newArray)-1):
            if newArray[i] >= newArray[i+1]:
                return False
        return True
        

    i = 0
    j = i+1
    while i<len(sequence)-1:
        if sequence[i] >= sequence[j]:
           result =  helper(sequence[:i]+sequence[j:]) or helper(sequence[:j]+sequence[j+1:])
           if not result:
                return False
        i+=1
        j+=1
    return True  

print(almostIncreasingSequence([1, 3, 2, 1]))
print(almostIncreasingSequence([1, 2, 3, 4, 3, 6]))
print(almostIncreasingSequence([3, 5, 67, 98, 3]))
print(almostIncreasingSequence([1, 4, 10, 4, 2]))
