"""
Pseudocode:
1. A: recursively sort half left list
2. B: recursively sort half right list
3. merge A and B
"""
def mergeSort(listNumbers):
    if len(listNumbers) > 1:
        # split the list
        left = listNumbers[:len(listNumbers)//2] 
        right = listNumbers[len(left):]
        # recursion
        left = mergeSort(left)
        right = mergeSort(right)
        #create array to save the list sorted
        listNumbers = []
        # while both sides has numers:
        while (len(left) and len(right)) > 0:
            if left[0] < right[0]:
                listNumbers.append(left[0])
                left.pop(0)
            else:
                listNumbers.append(right[0])
                right.pop(0)
        for i in left:
            listNumbers.append(i)
        for i in right:
            listNumbers.append(i)
    return listNumbers


listNumbers = [5,4,1,8,7,2,6,3]
print(mergeSort(listNumbers))

