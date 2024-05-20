from typing import List


class PacificAtlanticWaterFlow:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m: int = heights.__len__()
        n: int = heights[0].__len__()
        can_reach_pacific: List[List[bool]] = [[False for _ in range(n)] for _ in range(m)]
        can_reach_atlantic: List[List[bool]] = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            self._dfs(heights, can_reach_pacific, i, 0, m, n)
            self._dfs(heights, can_reach_atlantic, i, n - 1, m, n)

        for i in range(n):
            self._dfs(heights, can_reach_pacific, 0, i, m, n)
            self._dfs(heights, can_reach_atlantic, m - 1, i, m, n)

        result = []
        for i in range(m):
            for j in range(n):
                if can_reach_pacific[i][j] and can_reach_atlantic[i][j]:
                    result.append([i, j])
        return result

    def _dfs(self, heights: List[List[int]], can_reach: List[List[bool]], r: int, c: int, m: int, n: int):
        if can_reach[r][c]:
            return
        can_reach[r][c] = True
        for x, y in self.DIRECTIONS:
            next_r, next_c = r + x, c + y
            if 0 <= next_r <= m - 1 and 0 <= next_c <= n - 1 and heights[next_r][next_c] >= heights[r][c]:
                self._dfs(heights, can_reach, next_r, next_c, m, n)


if __name__ == "__main__":
    pacific_atlantic_water_flow = PacificAtlanticWaterFlow()
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(pacific_atlantic_water_flow.pacificAtlantic(heights))
