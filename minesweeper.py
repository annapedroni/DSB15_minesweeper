'''
function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot.
Return a grid, where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot i.e. (horizontally, vertically, and diagonally)
'''


# main function
def minesweeper(given_grid):
    for row in range(len(given_grid)):
        for col in range(len(given_grid[row])):
            if given_grid[row][col] not in ["#", "-"]:
                print("Unexpected element in the grid")
            elif given_grid[row][col] == "-":
                given_grid[row][col] = check_adjacent_spots(row, col, given_grid)

    return given_grid

# look into adjacent positions
def check_adjacent_spots(current_row, current_col, grid):
    
    # limits for conditionals
    max_index_of_rows = len(grid) - 1
    max_index_previous_row = None
    if current_row != 0:
        max_index_previous_row = len(grid[current_row-1]) - 1
    max_index_following_row = None
    if current_row < max_index_of_rows:
        max_index_following_row = len(grid[current_row+1]) - 1

    # counter
    adjacent_mines = 0
    
    # NW position
    if current_row != 0 and current_col != 0 and (current_col-1) <= max_index_previous_row:
        adjacent_mines = check_dash(current_row-1, current_col-1, grid, adjacent_mines)
    # N position
    if current_row != 0 and (current_col) <= max_index_previous_row:
        adjacent_mines = check_dash(current_row-1, current_col, grid, adjacent_mines)
    # NE position
    if current_row != 0 and current_col+1 <= max_index_previous_row:
        adjacent_mines = check_dash(current_row-1, current_col+1, grid, adjacent_mines)
    # W position
    if current_col != 0:
        adjacent_mines = check_dash(current_row, current_col-1, grid, adjacent_mines)
    # E position
    if current_col+1 <= len(grid[current_row])-1:
        adjacent_mines = check_dash(current_row, current_col+1, grid, adjacent_mines)
    # SW position
    if current_row+1 <= max_index_of_rows and (current_col-1) <= max_index_following_row:
        adjacent_mines = check_dash(current_row+1, current_col-1, grid, adjacent_mines)
    # S position
    if current_row+1 <= max_index_of_rows and (current_col) <= max_index_following_row:
        adjacent_mines = check_dash(current_row+1, current_col, grid, adjacent_mines)
    # SE position
    if current_row+1 <= max_index_of_rows and (current_col+1) <= max_index_following_row:
        adjacent_mines = check_dash(current_row+1, current_col+1, grid, adjacent_mines)
   
    return str(adjacent_mines)

# if "#"", increase counter
def check_dash(row, col, grid, counter):
    if grid[row][col] == "#":
            counter += 1
    return counter


# test grids
grid_00 = [["-"]]
grid_01 = [["#"]]
grid_02 = [["#"],["#"]]
grid_03 = [["#"], [0]]
grid_03 = [["#"], ["-"]]
grid_04 = [["#", "#", "-", "-"], ["#", "-", "-", "-"], ["#", "-", "-", "#"]]
grid_05 = [["#", "#", "-"], ["#", "-", "-", "-"], ["#", "-"]] # ragged list
grid_06 =  [["-", "-", "-", "#", "#"], ["-", "#", "-", "-", "-"], ["-", "-", "#", "-", "-"], ["-", "#", "#", "-", "-"], ["-", "-", "-", "-", "-"]]
grid_07 = [["-", "-", "-", "-"], ["-", "-", "-", "-"], ["-", "-", "-", "-"]]


# call the function and print the original grid and the resulting grid
print()
print(*grid_06, sep="\n")
print()
returned_grid = minesweeper(grid_06)
print(*returned_grid, sep="\n")  # https://stackoverflow.com/questions/22695171/print-list-elements-line-by-line-is-it-possible-using-format
print()