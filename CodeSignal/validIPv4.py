def isIPv4Address(inputString):
    splitted = inputString.split(".")
    
    # IPV4:
    # c1 : four parts
    # c2 : length bigger than 0 and dont start with zero
    # c3 : no letters
    # c4 : number between 0 and 255
    if len(splitted) != 4:
        return False
    i = 0
    while i < 4:
        if len(splitted[i]) == 0 :
            return False
        else:
            if len(splitted[i])>1 and splitted[i][0] == '0':
                return False
            elif splitted[i].isdigit() == False:
                return False 
            elif int(splitted[i]) < 0 or int(splitted[i])>255:
                return False
            i+=1
    return True

print(isIPv4Address("172.0.9.2"))
print(isIPv4Address("1a.10.9.2"))
print(isIPv4Address("267.0.0.0"))
print(isIPv4Address("00.0.1.2"))

