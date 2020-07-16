# Without using combinations from itertools

def fourNumberSum(array, targetSum):
    # Write your code here.
    sln = []
    for combination in combinationsFinder(array,4):
        if sum(combination) == targetSum:
            sln.append(combination)
    return sln


def combinationsFinder(lst, n): 
    if n == 0: 
        return [[]] 
    l =[] 
    for i in range(0, len(lst)): 
        # print("L: ", l)
        m = lst[i]
        remLst = lst[i + 1:]
        for p in combinationsFinder(remLst,n-1): 
            l.append([m]+p) 
    return l 

if __name__ == "__main__":
    array = [7, 6, 4, -1, 1, 2]
    targetSum = 16
    print(fourNumberSum(array, targetSum))