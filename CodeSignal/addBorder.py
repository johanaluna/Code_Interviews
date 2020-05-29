"""

"""


def addBorder(picture):
    temp = "*"*(len(picture[0]))
    
    n = len(picture)
    
    for i in range(n):
        pivot = picture[i]
        picture[i] = "*" + temp + "*"
        temp = pivot
    picture.append("*" + temp + "*")
    picture.append(picture[0])

    return picture

picture = ["abcde","fghij"]
print(addBorder(picture))