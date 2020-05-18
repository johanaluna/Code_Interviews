"""
isValidIP("0.0.0.0") ==> true
isValidIP("12.255.56.1") ==> true
isValidIP("137.255.156.100") ==> true
  
isValidIP('') ==> false
isValidIP('abc.def.ghi.jkl') ==> false
isValidIP('123.456.789.0') ==> false
isValidIP('12.34.56') ==> false
isValidIP('01.02.03.04') ==> false

"""
def isValidIP(string):
    info = string.split('.')

    if len(string) < 1:
        return(False)

    if len(info) == 4:
        for x in info:
            if x.isdigit() == False:
                return False  
            elif len(x) > 1 and x[0] == "0":
                return False
            elif x == "":
                return False 
            elif x.isdigit() == True and (int(x)>= 0 and  int(x)<=255):
                pass
            else: 
                return False
        return True
    else: return False



print(isValidIP("0.0.0.0"))
print(isValidIP("12.255.56.1"))
print(isValidIP("137.255.156.100"))
print(isValidIP(''))               # DONE
print(isValidIP('abc.def.ghi.jkl')) # DONE
print(isValidIP('123.456.789.0')) # DONE
print(isValidIP('12.34.56')) # DONE
print(isValidIP('01.02.03.04'))
print(isValidIP('12.34.56.'))
print(isValidIP('1.34.56.9'))