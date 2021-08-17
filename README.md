# Sudoku Solver

Determining the shortest distance between two points is a crucial aspect in day to day life. This application does exactly that. It determines the shortest distance between two points in any given obstacle using different approaches.

With this Pathfinding Algorithms application, users can draw unique obstacles or choose one of the preset ones, and the shortest path between the start point and endpoint will be determined.

The user also has the option to watch the solution unfold or to choose between algorithms such that they may see the differences between how each algorithm works.

### Tech Stack:
Frontend - Java Swing (GUI)

Backend - Java (Algorithms, Obstacles, and Features)

### Application's Functionality:
A settings component of the entire application allows the user to start the pathfinding, reset the board, see the steps of the solution, choose between different algorithms, and choose between different obstacles.

If a different obstacle is chosen, then the board resets, and the new obstacle is drawn instead. If a different algorithm is chosen, then the application remembers this algorithm for when the pathfinding begins.

The application has several different algorithms to choose from including:

- Breadth-First Search: Checks the board by viewing the tiles closest to the start tile, then spreading out
- Depth-First Search: Fully attempts one path until a dead end is reached, then attempts another
- A*: Calculates a G, H and F cost for the current tile, being the distances between the start/end tile and the current tile
- Dijkstra: Checks tiles that are closest to the start tile

Once an algorithm and obstacle are chosen, the user can then choose to see the steps or just view the solution. Seeing the steps will render red and green tiles to depict how the algorithm runs and which tiles it checks.
