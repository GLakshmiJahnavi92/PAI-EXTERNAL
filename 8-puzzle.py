import heapq
class PuzzleState:
    def __init__(self, board, goal, moves=0):
        self.board, self.goal, self.moves = board, goal, moves
    def __eq__(self, other):
        return self.board == other.board
    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())
    def __hash__(self):
        return hash(str(self.board))
    def heuristic(self):
        return sum(abs((val-1)//3 - i) + abs((val-1)%3 - j) for i, row in enumerate(self.board) for j, val in enumerate(row) if val)
    def get_next_states(self):
        i, j = next((i, j) for i, row in enumerate(self.board) for j, val in enumerate(row) if not val)
        next_states = []
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_board = [row[:] for row in self.board]
                new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                next_states.append(PuzzleState(new_board, self.goal, self.moves + 1))
        return next_states
def a_star(initial_state):
    open_set, closed_set = [], set()
    heapq.heappush(open_set, initial_state)
    while open_set:
        current_state = heapq.heappop(open_set)
        if current_state.board == current_state.goal:
            return current_state.moves
        closed_set.add(current_state)
        for next_state in current_state.get_next_states():
            if next_state in closed_set:
                continue
            heapq.heappush(open_set, next_state)
    return -1
initial_board = [[2, 3, 8], [1, 6, 4], [7, 0, 5]]
goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
initial_state = PuzzleState(initial_board, goal_board)
print("Number of moves:", a_star(initial_state))
print("intial_board:",initial_board)
for row in initial_board:
    print(row)
print("goal_board:",goal_board)
for row in goal_board:
    print(row)