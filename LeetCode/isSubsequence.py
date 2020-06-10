def isSubsequence(s, t):
    i = j = 0
        
    while i < len(s):
        if j == len (t):
            return False
            break
        elif s[i] is t[j]:
            i += 1
            j += 1
        else:
            j += 1
    return True


s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))