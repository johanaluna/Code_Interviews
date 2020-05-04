#!/bin/python3
"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors ar = 1,2,1,2,1,3,2. There is one pair of color and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available. sockMerchant has the following parameter(s):

n: the number of socks in the pile ar: the colors of each sock Sample input 9 10 20 20 10 10 30 50 10 20

Sample output 3

"""
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dictar={}
    for i in range(n):
        if ar[i] not in dictar.keys():
            dictar[ar[i]] = 1
        else:
            dictar[ar[i]] += 1
    count=0
    for a in dictar.values():
        count = count + (a//2)
    return count


if __name__ == '__main__':

    ar =[10, 20, 20, 10, 10, 30, 50, 10, 20]
    n= len(ar)
    print(sockMerchant(n, ar))