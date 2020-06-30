from itertools import permutations

def stringsRearrangement(inputArray):
    permu = permutations(inputArray)
    for p in permu:
        changes = [changer(p[i],p[i+1]) for i in range(len(p)-1)]
        if all(changes):
            return True
    return False
    
def changer(a,b):
    changes = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            changes += 1
    if changes ==1:
        return True
    return False

if __name__ == "__main__":
    a= ["aba", "bbb", "bab"]
    print(stringsRearrangement(a))