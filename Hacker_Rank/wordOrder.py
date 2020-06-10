"""
link: https://www.hackerrank.com/challenges/word-order/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
Input:
4
bcdef
abcdefg
bcde
bcdef

Output:
3
2 1 1
"""

n = int(input())
dictWord = {}
for i in range(n):
    word = input()
    if word in dictWord:
        dictWord[word] += 1
    else:
        dictWord[word] = 1

print(len(dictWord))
for i in dictWord.values(): 
    print(i, end=" ") 
