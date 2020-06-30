"""
Given a string, find the shortest possible string 
which can be achieved by adding characters to the 
end of initial string to make it a palindrome.
For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
"""

def buildPalindrome(st):
    if alreadyPalindrome(st):
        return st
    reverse = st[::-1]
    i = 0

    while i < len(st):
        if st[i:] == reverse[:len(st)-i]:
            return st + reverse[-i:]
        i+=1


    
def alreadyPalindrome(st):
    i = 0 
    j = len(st)-1
    while i < j :
        if st[i] != st[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == "__main__":
    st = "abcdc"
    print(buildPalindrome(st))