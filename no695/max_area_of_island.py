from typing import List


class MaxAreaOfIsland:

    DIRECTION = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area, self.dfs(rows, cols, r, c, grid))
        return max_area

    def dfs(self, rows: int, cols: int, r: int, c: int, grid: List[List[int]]) -> int:
        if grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        area: int = 1
        for dir in self.DIRECTION:
            next_r, next_c = r + dir[0], c + dir[1]
            if 0 <= next_r < rows and 0 <= next_c < cols:
                area += self.dfs(rows, cols, next_r, next_c, grid)
        return area


if __name__ == "__main__":
    max_area_of_island: MaxAreaOfIsland = MaxAreaOfIsland()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(max_area_of_island.maxAreaOfIsland(grid))
