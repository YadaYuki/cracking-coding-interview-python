# 8-2

def get_path_to_goal_recursion(row, col, grid, path_to_goal):
    if row < 0 or col < 0 or grid[row][col] == False:
        return False
    is_start = (row == 0) and (col == 0)

    if is_start or get_path_to_goal_recursion(row-1, col, grid, path_to_goal) or get_path_to_goal_recursion(row, col-1, grid, path_to_goal):
        path_to_goal.append((row, col))
        return True
    return False


def get_path_to_goal(grid):
    path_to_goal = []
    if get_path_to_goal_recursion(len(grid)-1, len(grid[0])-1, grid, path_to_goal) == True:
        return path_to_goal
    else:
        return None



if __name__ == "__main__":
    grid = [
        [True,False,True],
        [True,True,True],
        [True,False,True],
    ]
    print(get_path_to_goal(grid))

