def uniquePaths(m, n):
    path = [1 for i in range(m)]
    for i in range(n - 1): 
        for j in range(1, m):  
            path[j] += path[j - 1] 
    return path[m - 1]
 
if __name__ == "__main__":
    m=7
    n=3
    print(uniquePaths(m, n))