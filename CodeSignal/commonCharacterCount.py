from collections import Counter 
def commonCharacterCount(s1, s2):
    dictS1 = Counter(s1)
    counting = 0
    
    for string in s2:
        if string in dictS1:
            if dictS1[string] > 0:
                counting += 1
                dictS1[string] -= 1
            
    return counting

s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1, s2))