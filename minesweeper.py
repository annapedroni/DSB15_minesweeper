'''
function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot.
Return a grid, where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot i.e. (horizontally, vertically, and diagonally)
'''

def check_dash(row, col, grid, counter):
    if grid[row][col] == "#":
            counter += 1
    return counter


def check_adjacent_spots(current_row, current_col, grid):
    
    number_of_rows = len(grid)
    adjacent_mines = 0
    
    # NW position
    if current_row != 0 and current_col != 0 and len(grid[current_row-1]) >= (current_col-1):
        print("NW")
        adjacent_mines = check_dash(current_row-1, current_col-1, grid, adjacent_mines)
    # N position
    if current_row != 0 and len(grid[current_row-1]) >= (current_col):
        print("N")
        adjacent_mines = check_dash(current_row-1, current_col, grid, adjacent_mines)
    # NE position
    if current_row != 0 and current_col+1 <= len(grid[current_row-1]):
        print("NE")
        adjacent_mines = check_dash(current_row-1, current_col+1, grid, adjacent_mines)
    # W position
    if current_col != 0:
        print("W")
        adjacent_mines = check_dash(current_row, current_col-1, grid, adjacent_mines)
    # E position
    if current_col+1 < len(grid[current_row]):
        print(f"{current_col+1} <= {len(grid[current_row])}")
        print("E")
        adjacent_mines = check_dash(current_row, current_col+1, grid, adjacent_mines)
    # SW position
    if current_row+1 <= len(grid) and len(grid[current_row+1]) >= (current_col-1):
        print("SW")
        adjacent_mines = check_dash(current_row+1, current_col-1, grid, adjacent_mines)
    # S position
    if current_row+1 <= len(grid) and len(grid[current_row+1]) >= (current_col):
        print("S")
        adjacent_mines = check_dash(current_row+1, current_col, grid, adjacent_mines)
    # SE position
    if current_row+1 <= len(grid) and len(grid[current_row+1]) >= (current_col+1):
        print("SE")
        adjacent_mines = check_dash(current_row+1, current_col+1, grid, adjacent_mines)
   
    return adjacent_mines


given_grid = [["-"]]



#given_grid = input("grid (2d list of '#' and '-'): ")

for row in range(len(given_grid)):
    print(row)
    for col in range(len(given_grid[row])):
        print(col)
        if given_grid[row][col] == "-":
            given_grid[row][col] = check_adjacent_spots(row, col, given_grid)

print(given_grid)