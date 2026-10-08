from collections import deque

class PuzzleState:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.blank_position = puzzle.index(0)

    def __str__(self):
        return '\n'.join([' '.join(map(str, self.puzzle[i:i + 3])) for i in range(0, self.size, 3)])

    def move(self, direction):
        new_state = PuzzleState(list(self.puzzle))
        if direction == 'up' and new_state.blank_position >= 3:
            new_state.puzzle[new_state.blank_position], new_state.puzzle[new_state.blank_position - 3] = (
                new_state.puzzle[new_state.blank_position - 3],
                new_state.puzzle[new_state.blank_position],
            )
            new_state.blank_position -= 3
        elif direction == 'down' and new_state.blank_position < 6:
            new_state.puzzle[new_state.blank_position], new_state.puzzle[new_state.blank_position + 3] = (
                new_state.puzzle[new_state.blank_position + 3],
                new_state.puzzle[new_state.blank_position],
            )
            new_state.blank_position += 3
        elif direction == 'left' and new_state.blank_position % 3 != 0:
            new_state.puzzle[new_state.blank_position], new_state.puzzle[new_state.blank_position - 1] = (
                new_state.puzzle[new_state.blank_position - 1],
                new_state.puzzle[new_state.blank_position],
            )
            new_state.blank_position -= 1
        elif direction == 'right' and (new_state.blank_position + 1) % 3 != 0:
            new_state.puzzle[new_state.blank_position], new_state.puzzle[new_state.blank_position + 1] = (
                new_state.puzzle[new_state.blank_position + 1],
                new_state.puzzle[new_state.blank_position],
            )
            new_state.blank_position += 1
        else:
            return None
        return new_state

def breadth_first_search(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()
    limit = 5

    while queue:
        current_state, path = queue.popleft()

        if current_state.puzzle == goal_state.puzzle:
            return path

        visited.add(tuple(current_state.puzzle))

        for direction in ['up', 'down', 'left', 'right']:

            if len(path) == limit:
                break

            new_state = current_state.move(direction)

            if new_state and tuple(new_state.puzzle) not in visited:
                queue.append((new_state, path + [direction]))
        
        print(f'move {len(path)}', path)

    return None

if __name__ == '__main__':
    # Example usage:
    # initial_puzzle = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    initial_puzzle = [1,2,3,0,4,6,7,5,8]
    goal_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    initial_state = PuzzleState(initial_puzzle)
    goal_state = PuzzleState(goal_puzzle)

    solution_path = breadth_first_search(initial_state, goal_state)

    if solution_path:
        print(f"Solution Path: {solution_path}")
    else:
        print("No solution found.")