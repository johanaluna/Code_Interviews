    
    
"""
Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""
def isPalindrome(s):
    sln = []
    for i in s :
        if i.isalpha():
            sln.append(i.lower())
        elif i.isdigit():
            sln.append(i)
    if sln == sln[::-1]:
        return True
    return False
   
  

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = "ama"
    print(isPalindrome(s))
    print(isPalindrome(s2))
    # print(isPalindrome2(s3))
        