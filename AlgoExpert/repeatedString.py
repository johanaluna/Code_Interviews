"""
Repeated String Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first letters of Lilah's infinite string.

For example, if the string s='abcac' and n=10, the substring we consider is abcacabcac, the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.

Function Description Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat n: the number of characters to consider Sample Input 0 aba 10

Sample Output 0 7

Sample Input 1 a 1000000000000

Sample Output 1 1000000000000

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    # new = s*n
    count = 0
    times_s_in_n= n//len(s)
    def count_aes(s):
        aes = 0
        for i in s :
            if i == 'a':
                aes += 1
        return aes
    aes_in_s = count_aes(s)
    if aes_in_s==len(s):
        count = n
    else:
        x = n-(times_s_in_n * len(s))
        
        count = (times_s_in_n * aes_in_s) + count_aes(s[:x])
        
    return count
    

if __name__ == '__main__':

#     s = 'aba'
    s = 'aba'
    n = 10
    print(repeatedString(s, n))