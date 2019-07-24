# Game of Life
# This is a cellular automaton
# Project taken from (https://robertheaton.com/2018/07/20/project-2-game-of-life/)

import random
import time
import os
import glob
from colorama import Fore, init
init(convert = True)

# 1. Build a board with dead state cells and random state cells
def dead_state(width,height):
    board = []
    for x in range(0, height):
        row = []
        for y in range(0, width):
            row.append(0)
        board.append(row)
    return board

def random_state(width=150, height=150,threshold=0.5):
    board = []
    for x in range(0, height):
        row = []
        for y in range(0, width):
            random_number = random.uniform(0, 1)
            if random_number >= threshold:
                row.append(1)
            else:
                row.append(0)
        board.append(row)
    return board


# 2. Rendering the board into a pretty printing look, with the colored option enabled
def colored_cells():
    cell_value = '@'
    colors = list(vars(colorama.Fore).values())
    colored_cell_value = random.choice(colors) + cell_value
    return colored_cell_value
    
def render(state):
    render_matrix = []
    for row in state:
        render_row = []
        for element in row:
            if element == 1:
                #render_row.append('@')    # Option for monocolored chars
                render_row.append(colored_cells())
            else:
                render_row.append(' ')
        render_matrix.append(render_row)
    for row in render_matrix:
        print(' '.join(row))

        
# 3. Applying the rules to a new board, and returning a new state board
def next_board_state_moore(board):
    # Calculations based on the Moore neighborhood
    board_state = board.copy()
    width = len(board_state[0])
    height = len(board_state)
    new_state = dead_state(width,height)
    for x in range(0,len(board_state)):
        for y in range(0,len(board_state[x])):
            alive_neighbors = 0
            # Checking the upper left corner only, if above 0, it continues
            if (x - 1 >= 0) and (y - 1 >= 0):
                if board_state[x-1][y-1] == 1:
                    alive_neighbors += 1
            # Checking upper side, if above 0, it continues
            if (x - 1 >= 0):
                if board_state[x-1][y] == 1:
                    alive_neighbors += 1
            # Checking upper right corner
            if (x - 1 >= 0) and (y + 1 < len(board_state[x])):
                if board_state[x-1][y+1] == 1:
                    alive_neighbors += 1
            # Checking left side 
            if (y - 1 >= 0):
                if [y] != [0]:
                    if board_state[x][y-1] == 1:
                        alive_neighbors += 1
            # Checking right side
            if (y + 1 < len(board_state[x])):
                if board_state[x][y+1] == 1:
                    alive_neighbors += 1
            # Checking lower left side
            if (x + 1 < (len(board_state))) and (y - 1 >= 0):
                if board_state[x+1][y-1] == 1:
                    alive_neighbors += 1
            # Checking lower central side
            if (x + 1 < len(board_state)):
                if board_state[x+1][y] == 1:
                    alive_neighbors += 1
            # Checking lower right side
            if (x + 1 < len(board_state)) and (y + 1 < len(board_state[x])):
                if board_state[x+1][y+1] == 1:
                    alive_neighbors += 1
            # Deciding what to do with the count of alive neighbors
            if board_state[x][y] == 1:
                if alive_neighbors <= 1 or alive_neighbors > 3:
                    new_state[x][y] = 0
                else:
                    new_state[x][y] = 1
            if board_state[x][y] == 0:
                if alive_neighbors == 3:
                    new_state[x][y] = 1
    return(new_state)

def next_board_state_neumann(board):
    # Calculations based in the extended Von Neumann neighborhood
    board_state = board.copy()
    width = len(board_state[0])
    height = len(board_state)
    new_state = dead_state(width,height)
    for x in range(0,len(board_state)):
        for y in range(0,len(board_state[x])):
            alive_neighbors = 0
            # Checking upper slot
            if (x - 1 >= 0):
                if board_state[x-1][y] == 1:
                    alive_neighbors += 1
            # Checking left slot
            if (y - 1 >= 0):
                if [y] != [0]:
                    if board_state[x][y-1] == 1:
                        alive_neighbors += 1
            # Checking right slot
            if (y + 1 < len(board_state[x])):
                if board_state[x][y+1] == 1:
                    alive_neighbors += 1
            # Checking lower slot
            if (x + 1 < len(board_state)):
                if board_state[x+1][y] == 1:
                    alive_neighbors += 1
            # Deciding what to do with the count of alive neighbors
            if board_state[x][y] == 1:
                if alive_neighbors <= 1 or alive_neighbors > 3:
                    new_state[x][y] = 0
                else:
                    new_state[x][y] = 1
            if board_state[x][y] == 0:
                if alive_neighbors == 3:
                    new_state[x][y] = 1
    return(new_state)

# 4. Run it forever
def run_forever(initial_state):
    next_state = initial_state
    option = int(input('\n\nSelect the neighborhood:\n1 - Moore\'s Neighborhood\n2 - Von Neumann\'s Neighborhood\n'))
    if option == 1:
        while True:
            render(next_state)
            next_state = next_board_state_moore(next_state)
            time.sleep(0.001)
            os.system('cls')
    if option == 2:
        while True:
            render(next_state)
            next_state = next_board_state_neumann(next_state)
            time.sleep(0.001)
            os.system('cls')

        
# 5. This function collects a .txt pattern in the same directory as the script
def get_pattern():
    path = os.getcwd()
    extension = 'txt'
    result = glob.glob('*.{}'.format(extension))
    doc_path = path + '\\' + result[0]
    file = open(doc_path,'r')
    board = []
    for string in file:
        line = []
        for char in string:
            if char == '0' or char == '1':
                to_number = int(char)
                line.append(to_number)
        board.append(line)
    return board

# Example for Gosper's Glider Gun
glider_gun =\
[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]

# 6. Executing
if __name__ == '__main__':
    option = int(input('Select the option:\n1 - Random genereation\n2 - Get pattern from text\n3 - Gosper\'s Glider Gun example\n'))
    if option == 1:
        initial_state = random_state()
    if option == 2:
        initial_state = get_pattern()
        height = len(initial_state)
        width = len(initial_state[0])
    if option == 3:
        initial_state = glider_gun
    run_forever(initial_state)