class Solution(object):
    def floodFill(self, image, sr, sc, color):
        start_color = image[sr][sc]
        
        # If the starting pixel already has the target color, no need to do anything
        if start_color == color:
            return image

        def dfs(r, c):
            # Check boundaries and same color condition
            if (r < 0 or r >= len(image) or 
                c < 0 or c >= len(image[0]) or 
                image[r][c] != start_color):
                return
            
            # Fill the pixel with the new color
            image[r][c] = color
            
            # Explore 4-directionally
            dfs(r+1, c)  # Down
            dfs(r-1, c)  # Up
            dfs(r, c+1)  # Right
            dfs(r, c-1)  # Left

        dfs(sr, sc)
        return image

sol = Solution()
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print(sol.floodFill([[0,0,0],[0,0,0]], 0, 0, 0))
