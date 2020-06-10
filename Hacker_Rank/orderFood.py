"""
Exercise: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?h_r=next-challenge&h_v=zen

Sample input:
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample output:
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""

n = int(input())
dictFood = {}
for i in range(n):
    order = input().rsplit(' ', 1 )
    if order[0] in dictFood:
        dictFood[order[0]] += int(order[1])
    else:
        dictFood[order[0]] = int(order[1])

for k,v in dictFood.items():
    print(k +" "+ str(v))