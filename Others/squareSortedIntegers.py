# Questions to ask :
# is this a list of integers?
# are there negative numbers?

def squareList(array):
    right = 0
    sln = []
    while right < len(array) and array[right] < 0:
        right += 1
    left = right-1

    while len(sln) < len(array) or right is len(array)-1:
        print("left", left, "right", right)
        if array[left]**2 < array[right]**2:
            sln.append(array[left]**2)
            left -= 1
        else: 
            sln.append(array[right]**2)
            right += 1
    print(sln)


array = [ -10, -6, -5, 0, 2, 3]


squareList(array)