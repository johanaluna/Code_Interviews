"""
Given a string, find out if its characters can be rearranged to form a palindrome. 
palindromeRearranging(inputString) = true.

"""


def palindromeRearranging(inputString):
    dictionary = {}
    for string in inputString:
        if string not in dictionary:
            dictionary[string] = 1
        else:
            dictionary[string] += 1
            
    flag = 0 
    for k in dictionary.values():
        if k%2 != 0:
            if flag == 1:
                return False
            flag = 1
        
    return True