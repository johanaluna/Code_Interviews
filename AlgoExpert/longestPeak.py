def longestPeak(array):
    # Write your code here.
    i = 1
    maxi=0
    peaks=[]
    while i < len(array)-1:
        if array[i] > array[i-1] and array[i] > array[i+1]:
            peaks.append(i)
        i += 1
        
    maxi = 0
    for i in peaks:
        left = i-1
        right = i+1
        while left > 0 and array[left] > array[left-1]:
            left -=1
        while right < len(array)-1 and array[right] > array[right+1]:
            right +=1
        if (right -left)+1 > maxi :
            maxi = (right -left)+1
    return maxi

array= [0,1,2,3,0,14,1]
print(longestPeak(array))