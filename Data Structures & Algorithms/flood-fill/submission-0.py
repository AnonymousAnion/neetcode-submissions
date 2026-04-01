class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        og_color = image[sr][sc]

        def dfs(i: int, j: int) -> None:

            nonlocal image
            nonlocal color
            nonlocal og_color

            if min(i, j) < 0 or i >= len(image) or j >= len(image[0]):

                return

            if image[i][j] == og_color and image[i][j] != color:

                image[i][j] = color
                dfs(i - 1, j)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i, j + 1)

        dfs(sr, sc)
        
        return image