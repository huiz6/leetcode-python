from typing import List


class NumberOfProvinces:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n: int = isConnected.__len__()
        count = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                self._dfs(isConnected, i, visited)
                count += 1
        return count

    def _dfs(self, is_connected: List[List[int]], i: int, visited: List):
        visited[i] = True
        for k in range(is_connected.__len__()):
            if is_connected[i][k] and not visited[k]:
                self._dfs(is_connected, k, visited)


if __name__ == "__main__":
    number_of_provinces: NumberOfProvinces = NumberOfProvinces()
    is_connected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(number_of_provinces.findCircleNum(is_connected))
