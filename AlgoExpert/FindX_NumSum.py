# Find 2 numbers that sum target
def find2NumsSum(array, target):
    i = 0
    dict_sums = {}
    sln = []
    while i < len(array):
        if array[i] not in dict_sums.values():
            dict_sums[array[i]] = target - array[i]
        else: 
            sln.append([ array[i], target - array[i] ])   
        i += 1
    return(sln)



# Find 3 numbers that sum target
def find3Numbers(array, target): 
    arr_size = len(array)
    
    for i in range(0, arr_size-1): 
        # Find pair in subarray A[i + 1..n-1]  
        # with sum equal to sum - A[i] 
        s = set() 
        curr_sum = target - array[i] 
        for j in range(i + 1, arr_size): 
            if (curr_sum - array[j]) in s: 
                print("Triplet is", array[i],  
                        ", ", array[j], ", ", curr_sum-array[j]) 
                return True
            s.add(array[j]) 
        print(s)
      
    return False
  

# Find 4 numbers that sum target
def find4NumsSum(array, target):
    pass




array2 = [1,2,3,4,5,6,7,8] 
# print(find2NumsSum(array2, 9))

print(find3Numbers(array2, 13))