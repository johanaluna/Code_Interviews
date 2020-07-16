def islandPerimeter(grid):
    if len(grid)==0:
        return 0
        
    ans = 0 
    row = len(grid)
    column = len(grid[0])
    bigger = [[0]*(column+1)]  
    for g in grid:
        bigger.append([0]+g+[0])
    bigger.append([0]*(column+1))
    # print(bigger)
    for i in range(1,row+1):
        for j in range(1,column+1):
            if bigger[i][j]==1:
                if bigger[i+1][j]==0:
                    ans+=1
                if bigger[i-1][j]==0:
                    ans+=1
                if bigger[i][j+1]==0:
                    ans+=1
                if bigger[i][j-1]==0:
                    ans+=1
    return ans

if __name__ == "__main__":
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(islandPerimeter(grid))