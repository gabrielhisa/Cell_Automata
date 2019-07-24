# Cell_Automata

This is Conway's Game of Life / Cell Automata! This project's based on Robert Heaton's [Programming Projects for Advanced Beginners #2: Game of Life](https://robertheaton.com/2018/07/20/project-2-game-of-life/).

It is a complex cell automata based on simple rules:

 - Any live cell with 0 or 1 live neighbors dies
 - Any live cell with 2 or 3 live neighbors stays alive
 - Any live cell with more than 3 live neighbors dies
 - Any dead cell with exactly 3 live neighbors becomes alive
 
 These rules can lead to complex patterns, such as the Gosper's Glider Gun, contained in the code as an example. 
 
 Moore's neighborhood was used as the standard, considering the 8 immediate neighbors around the cell.
 
 The code alson contains:
 
  - A function for Von Neumann's extended neighborhood
  - Colored characters
  - The option to load patterns from .txt files, located in the directory of the program

It is worth mentioning that the code , with a 150 x 150 board, should be displayed without any issue in the prompt.
