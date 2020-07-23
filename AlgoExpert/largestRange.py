def largestRange(array):
    # Write your code here.
	# if len < 2:
	if len(array)<2:
		return [array[0],array[0]]
	# 1) Order Array
	array.sort()
	ranges = {}
# 	print(array)
	i = 0
	j = 1 
# 	maxi = [] 
	while j < len(array):
		if array[j] - array[j-1] == 1 or array[j] - array[j-1] == 0:
			if j == len(array)-1:
				ranges[array[i], array[j]] = array[j] - array[i]
			j+=1
		else:
			ranges[array[i], array[j-1]] = array[j-1] - array[i]
			i = j
			j += 1

	maxi = float("-inf")
	sln = []
	for k,v in ranges.items():
		if v >= maxi:
			maxi = v
			sln = [k[0],k[1]]
			
	return sln

if __name__ == "__main__":
    array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    print(largestRange(array))