"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

"""
from collections import Counter
def areSimilar(a, b):
    # conditions 
    c1 = len(a) != len(b)
    c2 = sum(a) != sum(b)
    c3 = Counter(a) != Counter(b)
    
    if c1 or c2 or c3:
        return False
    
    c = [0 if a[i]==b[i] else 1 for i in range(len(a))]
            
    if sum(c)> 2:
        return False
    return True
    

a = [1,3,2]
b=[1,2,3]


print(areSimilar(a, b))
