class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])

        visited = set()
        islands = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0":
                    continue
                if (row, col) in visited:
                    continue
                
                islands += 1
                queue = deque()
                queue.append((row, col))
                visited.add((row, col))

                while queue:
                    current_row, current_col = queue.popleft()

                    for row_change, col_change in directions:
                        next_row = current_row + row_change
                        next_col = current_col + col_change

                        if next_row < 0 or next_row >= rows:
                            continue
                        if next_col < 0 or next_col >= cols:
                            continue
                        if grid[next_row][next_col] == '0':
                            continue
                        if (next_row, next_col) in visited:
                            continue
                        
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))
        
        return islands
                        