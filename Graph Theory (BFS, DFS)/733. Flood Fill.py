# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

 

# Example 1:

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

# Output: [[2,2,2],[2,2,0],[2,0,1]]
# From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

# Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

# Example 2:

# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

# Output: [[0,0,0],[0,0,0]]

# Explanation:

# The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.



# DFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # nothing changed
        if image[sr][sc] == color:
            return image
        
        # old color of the grid
        old_color = image[sr][sc]
        rowMax, colMax = len(image), len(image[0])

        def dfs(r, c, color):
            # we only change the grid that has the same color as the old color
            # And we do a dfs on each direction
            # we will eventually converge because when the grid is new_color, it won't get into the dfs loop
            # 
            if image[r][c] == old_color:
                image[r][c] = color
                if r + 1 < rowMax:
                    dfs(r + 1, c, color)
                if r - 1 >= 0:
                    dfs(r - 1, c, color)
                if c + 1< colMax:
                    dfs(r, c + 1, color)
                if c - 1 >= 0:
                    dfs(r, c - 1, color)
            return 
        
        dfs(sr, sc, color)
        return image