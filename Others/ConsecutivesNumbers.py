# arr = [2,5,6]
# k = 10
# output = 4 --> 2,5,6,[2,5]
def findSubarrays(array, k):
    if len(array)==0 or array == None:
        return 0
    # init counter
    counter = 0
    
    #go through all values
    for i in range(1,len(array)):
        j = 0
        while j < len(array):
            # print("here", j, array[j:j+i])
            if sum(array[j:j+i])< k and len(array[j:j+i])== i:
                counter+=1
            j+=1
        i+=1
    return counter


def findSubarrays2(array, k):
    if len(array)==0 or array == None:
        return 0
    # init counter
    counter = 0
    init = 0
    i=0
    #go through all values
    while i < len(array):
        if array[i]<k:
            counter +=1
            if i > init and sum(array[init:i+1])<k:
                print("array[init:i+1]",array[init:i+1], sum(array[init:i+1]))
                counter += 1
                print("c",counter)
            elif sum(array[init:i+1])>k:
                init = i-1
        else:
            init = i+1
        i+=1
    return counter

if __name__ == "__main__":
    array = [2,5,6,7,1]
    array = [5,2,6,7,1]
    # array = [1, 11, 2, 3, 15]
    k = 10
    print(findSubarrays2(array, k))


