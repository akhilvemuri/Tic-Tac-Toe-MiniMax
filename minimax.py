board = [[0]*3 for i in range(3)]   
MIN = -1  # The human is the minimizing player
MAX = 1    # The AI is the maximizing player


def display_board(inputs):
    """
    Prints out tic-tac-toe board based on inputs (usually board state values)

    :param inputs: array of values to print on the board
    :return: None
    """
    mappings = {    # Mapping of player values to symbols
        -1: 'X',
         1: 'O',
         0: '-'
    }
    
    converted = [mappings[x] for x in inputs if x in mappings]
    if converted:   # Checks if the inputs are the board state values
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


def convert_board_to_input():
    """
    Helper function that converts board to inputs for display_board
    """
    return [board[0][0], board[0][1], board[0][2],
            board[1][0], board[1][1], board[1][2],
            board[2][0], board[2][1], board[2][2]]


def win(player, state):
    """
    Has a player has won the game

    :param player: MIN or MAX
    :param state: the current board
    :return: bool
    """
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
    """
    Any more spaces or has someone won

    :return: bool
    """
    return not empty_spaces(state) or win(MIN, state) or win(MAX, state)

def empty_spaces(state):
    """
    Finds all the empty cells on the board

    :return: array of [x, y] indices that have 0 value
    """
    empty = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                empty.append([i, j])
    
    return empty

def make_move(player, pos_x, pos_y):
    """
    Updates board for given player move

    :param pos_x: row index of move (int)
    :param pos_y: column index of move (int)
    :return: bool of whether move was successfully made
    """
    if [pos_x, pos_y] in empty_spaces(board):
        board[pos_x][pos_y] = player
        return True
    else:
        return False

def human_turn():
    """
    Asks for human player's move and updates board state accordingly
    """
    if is_game_over(board):
        return
    
    pos = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }
    
    while not (0 < pos < 10):   # Checks for any invalid inputs
        try:
            pos = int(input('Your Turn (X)! Enter a coordinate (1..9): '))
            coords = moves[pos]
            successful_move = make_move(MIN, coords[0], coords[1])

            if not successful_move:
                print('\nInvalid input. Please try again.')
                pos = -1
        except (KeyError, ValueError, TypeError):
            print('\nInvalid input. Please try again.')
        except (EOFError, KeyboardInterrupt):
            exit()


def minimax(state, depth, player):
    """
    Runs through decision tree using recursion and finds best
    possible move for the AI to play

    :return: array of [x_pos, y_pos, best_eval]
    """
    if depth == 0 or is_game_over(state):       # Base case
        if win(MAX, state):
            static_eval = 1
        elif win(MIN, state):
            static_eval = -1
        else:
            static_eval = 0
        # Returns static evaluation (-1 --> human win, +1 --> comp win, 0 --> draw)
        # of current position
        return [-1, -1, static_eval]

    if player == MAX:
        best_eval = [-1, -1, float('-inf')]     # Min initial for maximizing player
    else:
        best_eval = [-1, -1, float('inf')]      # Max initial for minimizing player

    for pos_x, pos_y in empty_spaces(state):
        state[pos_x][pos_y] = player
        curr_eval = minimax(state, depth - 1, -player)
        
        state[pos_x][pos_y] = 0     # Reset to empty state
        curr_eval[0], curr_eval[1] = pos_x, pos_y       # Add "best" pos_x & pos_y for AI's move

        if player == MAX:
            best_eval = max(best_eval, curr_eval, key=lambda x: x[2])
        else:
            best_eval = min(best_eval, curr_eval, key=lambda x: x[2])

    return best_eval


def comp_turn():
    """
    Plays AI's move using "best" pos_x & pos_y from minimax
    """
    if is_game_over(board):
        return
    
    move = minimax(board, len(empty_spaces(board)), MAX)
    pos_x, pos_y = move[0], move[1]
    
    print('Computer Turn (O):')
    make_move(MAX, pos_x, pos_y)    







def main():
    print("\nWelcome to Tic-Tac-Toe!")
    print("Here's a layout of the board for your reference.")
    display_board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    while not is_game_over(board):
        human_turn()
        display_board(convert_board_to_input())

        comp_turn()
        display_board(convert_board_to_input())

    if win(MIN, board):
        print("Congratualations, you've somehow beaten the unbeatable AI!")
    elif win(MAX, board):
        print("Game Over! You Lost.")
    else:
        print("Draw!")

    exit()

if __name__ == "__main__":
    main()