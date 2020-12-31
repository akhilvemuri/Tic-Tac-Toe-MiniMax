board = [[0]*3 for i in range(3)]
HUMAN = -1
COMP = +1


def convert_board_to_input():
    return [board[0][0], board[0][1], board[0][2],
            board[1][0], board[1][1], board[1][2],
            board[2][0], board[2][1], board[2][2]]

def display_board(inputs):
    
    mappings = {
        -1: 'X',
        +1: 'O',
         0: '-'
    }
    
    converted = [mappings[x] for x in inputs if x in mappings]
    if converted:
        inputs = converted
    inputs = [' {0} '.format(x) for x in inputs]
    
    print("""
      {0} | {1} | {2} 
      --------------- 
      {3} | {4} | {5} 
      ---------------   
      {6} | {7} | {8}   
    """.format(inputs[0], inputs[1], inputs[2],
               inputs[3], inputs[4], inputs[5],
               inputs[6], inputs[7], inputs[8]))


def win(player, state):
    win_states = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]]
    ]
    
    return [player]*3 in win_states
    
def is_game_over(state):
    return not empty_cells(state) or win(HUMAN, state) or win(COMP, state)

def empty_cells(state):
    empty = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                empty.append([i, j])
    
    return empty

def make_move(player, pos_x, pos_y):
    if [pos_x, pos_y] in empty_cells(board):
        board[pos_x][pos_y] = player
        return True
    else:
        return False

def human_turn():
    if is_game_over(board):
        return
    
    pos = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }
    
    while pos < 1 or pos > 9:
        try:
            pos = int(input('Your Turn (X)! Enter a coordinate (1..9): '))
            coords = moves[pos]
            moved = make_move(HUMAN, coords[0], coords[1])

            if not moved:
                print('\nBad input. Please try again.')
                pos = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError, TypeError):
            print('\nBad input. Please try again.')
            
def comp_turn():
    if is_game_over(board):
        return
    
    depth = len(empty_cells(board))
    if depth == 9:
        pos_x, pos_y = random.choice([0, 1, 2]), random.choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        pos_x, pos_y = move[0], move[1]
    
    print('Computer Turn (O).')
    make_move(COMP, pos_x, pos_y)
    
    
def minimax(state, depth, player):
    if player == COMP:
        best = [-1, -1, float('-inf')]
    else:
        best = [-1, -1, float('inf')]

    if depth == 0 or is_game_over(state):
        if win(COMP, state):
            score = +1
        elif win(HUMAN, state):
            score = -1
        else:
            score = 0
        return [-1, -1, score]

    for cell in empty_cells(state):
        pos_x, pos_y = cell[0], cell[1]
        state[pos_x][pos_y] = player
        
        score = minimax(state, depth - 1, -player)
        
        state[pos_x][pos_y] = 0
        score[0], score[1] = pos_x, pos_y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best    







def main():
    print("    Welcome to Tic-Tac-Toe!")
    display_board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    
    while not is_game_over(board):
        human_turn()
        display_board(convert_board_to_input())
        
        comp_turn()
        display_board(convert_board_to_input())

if __name__ == "__main__":
    main()