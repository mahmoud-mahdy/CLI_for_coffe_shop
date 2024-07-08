# sodoku_solver

The "Sudoku Solver" is a Python script developed as a personal project to enhance my programming skills in Python during my free time. This project focuses on efficiently solving Sudoku puzzles using a backtracking algorithm.

### How to Use:

⦁ Input Puzzle: Define the 'board' variable with the Sudoku puzzle, inserting '0' for empty cells.
  
⦁ Run Solver: Execute the script, triggering the backtracking algorithm to solve the Sudoku puzzle.

⦁ View Solution: The completed Sudoku solution is displayed through the 'print_board' function

### how the backtracking algorithm works:

⦁ Finding an Empty Cell: The algorithm locates an empty cell on the Sudoku board. If none exists, the puzzle is considered solved; otherwise, an empty cell is chosen.

⦁ Attempting Possible Solutions: It systematically tries numbers from 1 to 9 in the selected cell, verifying each against Sudoku rules. If a valid number is found, the 
  process continues to the next empty cell; otherwise, it backtracks.
  
⦁ Recursion and Backtracking: The algorithm recurs and explores different number combinations. When it hits a dead-end, it backtracks to the previous cell, trying alternative 
  numbers until a solution is reached.

⦁ By repeating these steps, the algorithm systematically fills in all empty cells, ultimately solving the Sudoku puzzle.
