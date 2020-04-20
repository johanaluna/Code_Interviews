"""
complexity O(2^n), O(n) space because we're storing all the n numbers 
"""

def getNthFib(n):
    # Write your code here.
	dictf = {}
	dictf[0] = 0
	dictf[1] = 1
	
	if n in dictf.keys():
		return dictf[n]
	else:
		return getNthFib(n-1) + getNthFib(n-2)

if __name__ == '__main__':

    n = 12
    print(getNthFib(n))
