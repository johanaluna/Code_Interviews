def boxBlur(image):
    i = 0
    results2 =[]
    pairs = len(image)-2
    p = len(image[0])-2
    while i < pairs:
        j = 0
        results = []
        while j < p:
            results.append((sum(image[i][j:j+3]) + sum(image[i+1][j:j+3]) + sum(image[i+2][j:j+3]))//9)
            j += 1
        results2.append(results)
        i+=1
    return results2

if __name__ == "__main__":
    # image = [[1,1,1], [1,7,1], [1,1,1]]
    image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
    print(boxBlur(image))