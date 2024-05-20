from typing import List


class WordSearch:

    DIRECTIONS = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = board.__len__()
        columns = board[0].__len__()
        exist = False
        for r in range(rows):
            for c in range(columns):
                visited = [[False for _ in range(columns)] for _ in range(rows)]
                visited[r][c] = True
                temp_str = board[r][c]
                exist |= self._back_tracking(board, visited, word, temp_str, r, c, rows, columns)
        return exist

    def _back_tracking(
            self, board: List[List[str]], visited: List[List[bool]], word: str, temp_str: str, r: int, c: int,
            rows: int, columns: int
    ) -> bool:
        if temp_str == word:
            return True
        elif word.startswith(temp_str):
            result = False
            for direction in self.DIRECTIONS:
                next_r, next_c = r + direction[0], c + direction[1]
                if 0 <= next_r < rows and 0 <= next_c < columns and not visited[next_r][next_c]:
                    temp_str += board[next_r][next_c]
                    visited[next_r][next_c] = True
                    result |= self._back_tracking(board, visited, word, temp_str, next_r, next_c, rows, columns)
                    temp_str = temp_str[:-1]
                    visited[next_r][next_c] = False
            return result
        else:
            return False


if __name__ == "__main__":
    word_search = WordSearch()
    board1: List[List[str]] = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word1: str = "ABCCED"
    print(word_search.exist(board1, word1))
