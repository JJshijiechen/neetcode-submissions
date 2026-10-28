class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        # Store the width and height of the board
        self.width = width
        self.height = height
        # Store the food list and a pointer to the next food
        self.food = food
        self.food_index = 0
        # Initialize the snake's position as a deque (head at front)
        self.snake = deque()
        self.snake.append((0, 0))  # start position
        # Set for O(1) collision checks
        self.snake_set = set()
        self.snake_set.add((0, 0))
        # Current score
        self.score = 0
        # Direction map
        self.dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        # Game over flag
        self.game_over = False

    def move(self, direction: str) -> int:
        # If already game over, just return -1
        if self.game_over:
            return -1
        
        # Get current head position
        head_r, head_c = self.snake[0]
        dr, dc = self.dirs[direction]
        new_r, new_c = head_r + dr, head_c + dc
        
        # Check for wall collision
        if not (0 <= new_r < self.height and 0 <= new_c < self.width):
            self.game_over = True
            return -1
        
        # Check for eating food
        eat = (self.food_index < len(self.food) and 
               [new_r, new_c] == self.food[self.food_index])
        
        # If not eating food, move tail
        if not eat:
            tail = self.snake.pop()
            self.snake_set.remove(tail)
        # Check for self collision (now tail is moved)
        if (new_r, new_c) in self.snake_set:
            self.game_over = True
            return -1
        
        # Add new head position
        self.snake.appendleft((new_r, new_c))
        self.snake_set.add((new_r, new_c))
        
        # If eating food, increment food index and score
        if eat:
            self.food_index += 1
            self.score += 1
        # Return current score
        return self.score