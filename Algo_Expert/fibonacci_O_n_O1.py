
"""
Complexity O(n), O(1) space because we're storing just the last 2 numbers
"""
def getNthFib(n):
    last_2n = [0, 1]
    counter = 2 #because we start with 2 values and we want to find the 3rd
    while counter <= n:
        newfib = last_2n[0] + last_2n[1] 
        last_2n[0] = last_2n[1]
        last_2n[1] = newfib
        counter += 1
    return last_2n[1] if n >1 else last_2n[0]

if __name__ == '__main__':

    n = 12
    print(getNthFib(n))