def sumTriangle(triangle):
    with open(triangle, 'r') as triangle:
        for triangleRow in triangle.readlines():
            outRow = triangleRow.strip().split()
            yield [int(x) for x in outRow]
            # yield list(map(lambda x: int(x), outRow))
        
def triangleReduce(topRow,bottomRow):
    pass
    # for i in range(len(bottomRow)):


if __name__ == "__main__":
    arrayT = sumTriangle("/Users/johanaluna/Documents/LAMBDA_2019/Code_Interviews/Others/triangle.txt")
    for t in arrayT:
        print(t)