import pdb

class PuzzleState:  
    def __init__(self, puzzle, cost=0, heuristic=0):
        self.puzzle = puzzle
        self.cost = cost
        self.heuristic = heuristic
        self.blk = puzzle.index(0)

    def __str__(self):
        txt = ''
        for i in range(0, 3, 3):
            for j in range(3):
                if j > 0:
                    txt += ' '
                txt += str(self.puzzle[j+i])
            txt += '\n'
        return txt

        # return '\n'.join([' '.join(map(str, self.puzzle[i:i + 3])) 
        #     for i in range(0, 3, 3)])

    def move(self, direction):
        new_state = PuzzleState(list(self.puzzle))
        if direction == 'up' and new_state.blk >= 3:
            new_state.puzzle[new_state.blk], new_state.puzzle[new_state.blk - 3] = (
                new_state.puzzle[new_state.blk - 3],
                new_state.puzzle[new_state.blk],
            )
            new_state.blk -= 3
        elif direction == 'down' and new_state.blk < 6:
            new_state.puzzle[new_state.blk], new_state.puzzle[new_state.blk + 3] = (
                new_state.puzzle[new_state.blk + 3],
                new_state.puzzle[new_state.blk],
            )
            new_state.blk += 3
        elif direction == 'left' and new_state.blk % 3 != 0:
            new_state.puzzle[new_state.blk], new_state.puzzle[new_state.blk - 1] = (
                new_state.puzzle[new_state.blk - 1],
                new_state.puzzle[new_state.blk],
            )
            new_state.blk -= 1
        elif direction == 'right' and (new_state.blk + 1) % 3 != 0:
            new_state.puzzle[new_state.blk], new_state.puzzle[new_state.blk + 1] = (
                new_state.puzzle[new_state.blk + 1],
                new_state.puzzle[new_state.blk],
            )
            new_state.blk += 1
        else:
            return None
        return new_state
    
# mahalanobis distance
def mh_dist(init, goal):
    manhattan_sum = 0
       
    for i in range(len(init)):
        value = init[i]
        pos = goal.index(value)
        manhattan_sum += abs(pos//3 - i//3) + abs(pos%3 - i%3) 

    return manhattan_sum

def depth_first_search(initial_state, goal_state):
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        current_state, path = stack.pop()

        if current_state.puzzle == goal_state.puzzle:
            return path

        visited.add(tuple(current_state.puzzle))
        
        heuristic_stack = []
        for direction in ['up', 'down', 'left', 'right']:
            new_state = current_state.move(direction)

            if new_state and tuple(new_state.puzzle) not in visited:
                new_state.cost = current_state.cost + 1
                new_state.heuristic = mh_dist(new_state.puzzle, goal_state.puzzle)
                heuristic_stack.append((new_state.cost+new_state.heuristic, direction, new_state))
                
        heuristic_stack.sort(key=lambda x: x, reverse=True)
        
        for (key, direction, state) in heuristic_stack: 
            stack.append((state, path + [direction]))

    return None

# only run directly, __name__ variable is set to bet '__main__'
# when it was imported, the __name__ will be set to file name (depth_8p)
if __name__ == '__main__':
    # Example usage:
    # initial_puzzle = [1, 2, 3, 4, 0, 5, 6, 7, 8] # y
    # initial_puzzle =  [1, 2, 3, 4, 5, 6, 0, 7, 8] # y
    # initial_puzzle =  [1, 2, 3, 0, 5, 6, 4, 7, 8] # y
    # initial_puzzle =  [1, 2, 3, 0, 5, 6, 4, 7, 8] # y
    # initial_puzzle =  [1, 2, 3, 4, 5, 6, 0, 7, 8] # y
    # initial_puzzle =  [1, 2, 3, 4, 5, 6, 0, 8, 7]
    # initial_puzzle =  [1, 2, 3, 4, 5, 6, 0, 7, 8]
    initial_puzzle =  [1, 0, 3, 5, 2, 6, 4, 7, 8] # y
    goal_puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0] # y

    initial_state = PuzzleState(initial_puzzle, 0, 0)
    goal_state = PuzzleState(goal_puzzle, 0, 0)

    solution_path = depth_first_search(initial_state, goal_state)

    if solution_path:
        print(f"Solution Path: {solution_path}")
    else:
        print("No solution found.")
