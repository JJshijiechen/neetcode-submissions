class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
                return False
            
            
            board[r][c] = '#'
            found = (dfs(r + 1, c, idx + 1) or
                dfs(r-1, c , idx + 1) or
                dfs(r, c+ 1, idx + 1) or
                dfs(r, c - 1, idx + 1))

            board[r][c] = word[idx]
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False