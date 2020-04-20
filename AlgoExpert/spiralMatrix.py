def spiralTraverse(array):
	result = []
	row = len(array)
	if row ==0:
		return result
	column = len(array[0])
	a,b = 0,0
	while a < column and b < row:
		# Go right 
		for i in range(a , column):
			result.append(array[a][i])
		b += 1
	
		# Go down 
		for i in range(b,row):
			result.append(array[i][column-1])
		column -= 1
	
		# Go left 
		if b < row:
			for i in range(column-1, a-1, -1):
				result.append(array[row-1][i])			
		row -= 1
		
		# Go up 
		if a< column:
			for i in range(row-1, b-1, -1):
				result.append(array[i][a])
			a +=1
	return result

array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
print(array,"\n", spiralTraverse(array))