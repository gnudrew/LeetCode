class Solution(object):
               
    def explore(self, i, j):
        # Mark current tile as explored
        self.tilesExplored[j][i] = True
        # Let's recursively go to available adjacent land tiles
        # check for grid edge and land adjacency
        if i+1 < self.n:
            if self.grid[j][i+1] == "1" and self.tilesExplored[j][i+1] == False:
                self.explore(i+1,j)
        if j+1 < self.m:
            if self.grid[j+1][i] == "1" and self.tilesExplored[j+1][i] == False:
                self.explore(i,j+1)
        if i-1 >= 0:
            if self.grid[j][i-1] == "1" and self.tilesExplored[j][i-1] == False:
                self.explore(i-1,j)
        if j-1 >= 0: 
            if self.grid[j-1][i] == "1" and self.tilesExplored[j-1][i] == False:
                self.explore(i,j-1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        # get grid dimensions. m x n
        self.m = len(grid) # m is number of rows (y-dimension)
        self.n = len(grid[0]) # n is number of columns (x-dimension)
        
        # initialize grid to track what we've explored so far
        self.tilesExplored = [ [ False for i in range(self.n) ] for j in range(self.m) ]
        
        numIslands = 0 # initialize island counter
        
        # Identify islands
        for i in range(self.n):
            for j in range(self.m):
                if ( self.grid[j][i] == "1" ) and ( self.tilesExplored[j][i] == False ):
                # explore the island, starting at tile (i,j)
                    self.explore(i,j)
                    # add to counter
                    numIslands = numIslands + 1
                    
        return numIslands