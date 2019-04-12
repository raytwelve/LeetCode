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
        lands = set() #every '1' on the whole graph
        for i in range(x):
            for j in range(y):
                if grid[i][j] == land and (i,j) not in lands:
                    # found a piece of land that we have not already discovered
                    # its a new island!
                    thisIsland = set()
                    thisIsland.add((i,j))
                    # lets explore!
                    self.findLands(thisIsland, lands, grid, x, y)
                    islands +=1
        return islands
    
    def findLands(self, thisIsland, lands, grid, x, y):
        land = "1"
        
        # exploreNext will be the land we need to explore in the next loop iteration
        exploreNext = set(thisIsland)

        while len(exploreNext) > 0:
            # we want to iterate thru exploreNext, but we will also have a new set of lands to explore in the next iteration
            # for x in exploreNext. find the lands to the up,down,left,right of it (we will need to explore these next)
            # since we are iterating thru exploreNext, we cannot update it with the next iterations pieces of land.. we dont want to visit the land we have already visited in this iteration


            newLands = set(exploreNext)
            exploreNext = set()
            for (i, j) in newLands:
                discoveredNewLands = set() #used within each iteration of this for loop
                
                # make copies to increment, then comeback to the original piece
                ii = i
                jj = j

                ii = i+1 #keep exploring to the south
                while ii < x and grid[ii][jj] == land and (ii,jj) not in thisIsland:
                    discoveredNewLands.add((ii,jj))
                    ii += 1

                ii = i-1
                while ii > -1 and grid[ii][jj] == land and (ii,jj) not in thisIsland:
                    discoveredNewLands.add((ii,jj))
                    ii += 1
                
                ii = i #reset to original

                jj = j+1
                while jj < y and grid[ii][jj] == land and (ii,jj) not in thisIsland:
                    discoveredNewLands.add((ii,jj))
                    jj += 1

                jj = j-1
                while jj > -1 and grid[ii][jj] == land and (ii,jj) not in thisIsland:
                    discoveredNewLands.add((ii,jj))
                    jj += 1
                jj = j
                

                # for each piece of land we have, we will have a set of lands we discovered. we keep adding these to one big collection  'exploreNext'
                exploreNext.update(discoveredNewLands)
                
                # thisIsland is all the pieces of land we find in this function call; aka summation of every set of discoveredNewLands... + the original piece of land we came into the function with
                # this is used to make sure we dont check them again in the succeeding loop iterations
                thisIsland.update(discoveredNewLands)

        # weve finally found all the water boarders! add it to the total lands we come across.
        # passed by reference, so nothing to return
        lands.update(thisIsland)