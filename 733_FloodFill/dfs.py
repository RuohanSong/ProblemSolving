from typing import List

# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        originalcolor = image[sr][sc]
        if originalcolor == color:
            return image

        def dfs(i, j):
            if image[i][j] == originalcolor:
                image[i][j] = color
                if i - 1 >= 0:
                    dfs(i - 1, j)
                if i + 1 < M:
                    dfs(i + 1, j)
                if j - 1 >= 0:
                    dfs(i, j - 1)
                if j + 1 < N:
                    dfs(i, j + 1)

        dfs(sr, sc)
        return image


# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr, sc, color = 1, 1, 2

image = [[0,0,0],[0,0,0]]
sr, sc, color = 0, 0, 0

print(Solution().floodFill(image, sr, sc, color))