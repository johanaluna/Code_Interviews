def isValidSubsequence(array, sequence):
    # Write your code here.
    seen=0
    i = j = 0 
    while i < len(sequence):
        if sequence[i] == array[j]:
            seen += 1
            i += 1
        if j == len(array)-1:
            break
        j += 1	
    if seen ==len(sequence): return True
    else: return False


array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]
print(isValidSubsequence(array, sequence))