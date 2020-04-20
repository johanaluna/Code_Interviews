"""
complexity O(n), O(n) space because we're storing all the n numbers 
"""
def getNthFib(n, dictn={1:1,2:1}):
    if n in dictn:
        return dictn[n]
    else:
        return getNthFib(n-1, dictn) + getNthFib(n-2, dictn)

if __name__ == '__main__':

    n = 12
    print(getNthFib(n))