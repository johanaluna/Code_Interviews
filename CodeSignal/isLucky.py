"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.
For n = 1230, the output should be
isLucky(n) = true;

For n = 239017, the output should be
isLucky(n) = false.

"""

def isLucky(n):
    middle = len(str(n))//2
    left = [int(str(n)[i]) for i in range(middle)]
    right = [int(str(n)[i]) for i in range(middle,len(str(n)))]
    
    return(True if sum(left) == sum(right) else False)

n = 239017
print(isLucky(n))