def binarySearch(array, target, index = 0):
	endIndex = len(array)-1
	while index <= endIndex:
		middle = (index + endIndex)//2
		
		if target > array[middle]:
			index = middle + 1
		elif target < array[middle]:
			endIndex = middle - 1
		else:
			return middle
	return -1

array = [1,2,3,4,5,6,88,230,289]
target = 88	
print(binarySearch(array, target, index = 0))