"""
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are 
equally strong (the strongest arm can be both the right and the left), 
and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
"""

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    # conditions 
    c1 = (yourLeft == friendsLeft) and (yourRight == friendsRight)
    c2 = (yourLeft == friendsRight) and (yourRight ==friendsLeft)
    return(True if c1 or c2 else False)

yourLeft = 10
yourRight = 15
friendsLeft = 15
friendsRight = 10

print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))

