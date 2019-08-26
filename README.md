# Sudoku solver using backtracking algorithm
Simple sudoku solver that uses [backtracking algorithm](https://www.geeksforgeeks.org/backtracking-algorithms/). This is a great example of how backtracking algorithm can solve [Constraint Satisfaction Problems](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem).

# How it works
It iterates through the board from the top most row and within each row goes from left to right most cell. Empty cells are marked with ".". For each empty cell it finds, it tries a number from 1 to 9, checks whether it's a valid entry, then moves on to the next cell. It does so recursively as can be seen on line 26 of sudokuSolver.py. </br>
""
if solve(board):
    return True
""
</br>
If at any stage of solving the sudoku board it hits a dead end / constraints can't be satisfied with the given combination of entries, the function returns false and backtracks to the entry that lead to the dead end and continues with proceeding numbers and repeats till a solution is found.

# Credits
I stumbled upon this question on Leetcode and adapted the code from this [post](https://leetcode.com/problems/sudoku-solver/discuss/15752/Straight-Forward-Java-Solution-Using-Backtracking).
