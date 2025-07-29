from flask import Flask, render_template, request
import copy

app = Flask(__name__)

# Solver logic
def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_safe(grid, row, col, num):
    if num in grid[row]:
        return False

    if num in [grid[i][col] for i in range(9)]:
        return False

    box_row_start = row - row % 3
    box_col_start = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[box_row_start + i][box_col_start + j] == num:
                return False

    return True

def solve_sudoku(grid):
    empty = find_empty_location(grid)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solution = None
    message = ""

    if request.method == 'POST':
        try:
            for i in range(9):
                for j in range(9):
                    val = request.form.get(f'cell-{i}-{j}')
                    if val and val.strip() != "":
                        grid[i][j] = int(val)
            grid_copy = copy.deepcopy(grid)
            if solve_sudoku(grid_copy):
                solution = grid_copy
            else:
                message = "❌ No solution exists for the given puzzle!"
        except ValueError:
            message = "Invalid input! Please enter numbers only."

    return render_template('index.html', grid=grid, solution=solution, message=message)

if __name__ == '__main__':
    app.run(debug=True)
