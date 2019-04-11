'''
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x = len(grid)
        if x == 0:
            return 0
        y = len(grid[0])
        islands = 0
        land = "1"
        lands = set()
        for i in range(x):
            for j in range(y):
                if grid[i][j] == land and (i,j) not in lands:
                    thisIsland = set()
                    thisIsland.add((i,j))
                    self.findLands(thisIsland, lands, grid, x, y)
                    islands +=1
        return islands
    
    def findLands(self, thisIsland, lands, grid, x, y):
        land = "1"
        
        exploreNext = set(thisIsland)
        while len(exploreNext) > 0:
#             cannot change set while iterating thru, create one to track 
            newLands = set(exploreNext)
            exploreNext = set()
            for (i, j) in newLands:
                discoveredNewLands = set()
                ii = i
                jj = j

                ii = i+1
                while ii < x and grid[ii][jj] == land and (ii,jj) not in thisIsland:
                    discoveredNewLands.add((ii,jj))
                    ii += 1

                ii = i-1
                while ii > -1 and grid[ii][jj] == land and (ii,jj) not in thisIsland:
                    discoveredNewLands.add((ii,jj))
                    ii += 1
                ii = i

                jj = j+1
                while jj < y and grid[ii][jj] == land and (ii,jj) not in thisIsland:
                    discoveredNewLands.add((ii,jj))
                    jj += 1

                jj = j-1
                while jj > -1 and grid[ii][jj] == land and (ii,jj) not in thisIsland:
                    discoveredNewLands.add((ii,jj))
                    jj += 1
                jj = j
                
                exploreNext.update(discoveredNewLands)
                thisIsland.update(discoveredNewLands)
        lands.update(thisIsland)