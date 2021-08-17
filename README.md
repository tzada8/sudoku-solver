# Sudoku Solver

Ever be doing a Sudoku puzzle and end up getting stuck in solving it? Well, this application aids the user in solving any Sudoku puzzle. 

With this Sudoku Solver application, a user can input any sudoku board they would like, and the program will solve the board for them using the Backtracking alogrithm. If no solution exists, then the application will inform the user of that.

The user also has the option to watch the solution unfold or to immediately see the answer to the puzzle.

### Tech Stack:
Frontend - Tkinter (GUI)

Backend - Python (Backtracking, Functionality, and Features)

### Application's Functionality:
There are two main settings of the application: a "Solve" button and a "Create" button:
- "Solve" prompts the user whether they would like to watch the solution unfold or just see the final answer, and then uses the Backtracking algorithm to physically solve the board
- "Create" opens a new window with an empty board, allowing the user to insert the numbers for their Sudoku puzzle.

Once the board is created, the user can then choose to see the steps or just view the solution. Seeing the steps will render red and green tiles to depict how the algorithm runs and which numbers it inserts/removes.
