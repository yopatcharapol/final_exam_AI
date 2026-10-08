import numpy as np
import pdb

class PuzzleNode:
    def __init__(self, state, cost=0, heuristic=0):
        self.state = state
        self.cost = cost
        self.heuristic = heuristic

    # less than for instance obj1 < obj2 when obj1 and obj2 are PuzzleNode
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
    
    def __eq__(self, candidate):
        return self.state == candidate.state

    
# manhattan_distance
def mh_dist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def find_pos(state, value=0):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == value:
                return (i, j)

def find_pos_np(state, value=0):
    return (state == 0).nonzero()

def get_dist(init, goal):
    manhattan_sum = 0
       
    for i in range(len(init)):
        for j in range(len(init[0])):
            value = init[i][j]
            find_pos = find_pos_np(goal, value)
            manhattan_sum += mh_dist((i, j), find_pos)

    return manhattan_sum


def gen_child(node, goal_state):
    children = []
    i = 0
    while 0 not in node.state[i]:
        i += 1

    row = i
    col = node.state[i].index(0)

    actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    for action in actions:
        nrow, ncol = (row + action[0], col + action[1])

        if 0 <= nrow < 3 and 0 <= ncol < 3:
            new_state = [list(row) for row in node.state]
            new_state[row][col] = new_state[nrow][ncol]
            new_state[nrow][ncol] = 0
            child_node = PuzzleNode(
                new_state,
                parent=node,
                action=action,
                cost=node.cost + 1,
                heuristic=get_dist(new_state, goal_state),
            )
            children.append(child_node)

    return children


def a_star_search(initial, goal):
    stack = [initial]
    closed_set = set()

    while stack:
        current_node = stack.pop()

        if current_node == goal:
            return get_solution_path(current_node)
        
        tp = tuple(current_node.state)
        closed_set.add(tp)

        children = gen_child(current_node, goal)
        
        heuristics = []
        _children = []
        for child in children:
            if child not in closed_set:
                _children.append(child)
                heuristics.append(child.heuristic)
        
        indx = np.argsort(-1*np.array(heuristics))

        stack.extend([_children[i] for i in indx])

    return None


def get_solution_path(node):
    path = []
    while node.parent is not None:
        path.insert(0, (node.action, node.state))
        node = node.parent
    return path


if __name__ == "__main__":
    # initial_state = [[2, 3, 5], [1, 4, 6], [7, 8, 0]] # 8 steps
    # initial_state = [[1, 3, 2], [4, 5, 6], [7, 8, 0]] # no solution
    # initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]] # 818 steps
    # initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]] # 8 steps
    # initial_state = [[1, 2, 3], [7, 4, 6], [0, 5, 8]] # 4 steps
    # initial_state = [[2, 3, 5], [4, 6, 0], [1, 7, 8]] # 8 steps
    
    # initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8] 
    # initial_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    # initial_state = [1, 2, 3, 0, 5, 6, 4, 7, 8]
    # initial_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    initial_state = [1, 2, 3, 4, 5, 6, 0, 8, 7] # N
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    initial = PuzzleNode(initial_state)
    goal = PuzzleNode(goal_state)
    
    solution_path = a_star_search(initial, goal)

    # if solution_path:
        
    #     for step in solution_path:
    #         print(f"Move {step[0]}:")
    #         for row in step[1]:
    #             print(row)
    #         print("------")
        
    #     print(f"Solution found in {len(solution_path)} moves")
    # else:
    #     print("No solution found.")
