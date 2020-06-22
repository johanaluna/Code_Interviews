def allLongestStrings(inputArray):
    maxi = 0
    strings = []
    for i in range(len(inputArray)):
        if len(inputArray[i]) > maxi:
            maxi = len(inputArray[i])
            strings = []
            strings.append(inputArray[i])
        elif len(inputArray[i]) == maxi:
            strings.append(inputArray[i])
        else: 
            pass
    return strings


inputArray= ["aba", 
 "aa", 
 "ad", 
 "vcd", 
 "aba"]

print(allLongestStrings(inputArray))