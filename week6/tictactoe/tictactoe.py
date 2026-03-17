"""
Tic Tac Toe Player
"""
import copy
import math

# Constants representing the two players and an empty cell
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    count_X = 0
    count_O = 0

    # Count the number of X and O marks on the board
    for row in board:
        for cell in row:
            if cell == X:
                count_X += 1
            elif cell == O:
                count_O += 1

    # Determine whose turn it is# Determine whose turn it is
    if count_X == count_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    # Iterate through the board and collect empty positions
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception

    current_player = player(board)

    # Create a copy of the board to avoid mutating the original
    new_board = copy.deepcopy(board)

    i, j = action

    # Apply the move
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check the rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
    
    # Check the columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If someone has won, the game is finished
    if winner(board) != None:
        return True

    # If there are still empty cells, the game continues
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
            
    # No empty cells and no winner, so draw
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)

    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)

    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If the game is already finished, no move can be made
    if terminal(board):
        return None

    current_player = player(board)

    best_action = None

    if current_player == X:
        best_score = float("-inf")

        for action in actions(board):
            score = min_value(result(board, action))

            if score > best_score:
                best_score = score
                best_action = action

    else:
        best_score = float("inf")

        for action in actions(board):
            score = max_value(result(board, action))

            if score < best_score:
                best_score = score
                best_action = action

    return best_action


def explain_move(board):
    """
    Returns (best_action, explanation)
    """

    if terminal(board):
        return None, "Game is already over."

    current = player(board)
    opponent = O if current == X else X

    best_action = minimax(board)

    # --- Helper: check if a move leads to a win ---
    def is_winning_move(board, action, p):
        new_board = result(board, action)
        return winner(new_board) == p

    # --- 1. Immediate win ---
    if is_winning_move(board, best_action, current):
        return best_action, "This move wins the game immediately."

    # --- 2. Block opponent win ---
    for action in actions(board):
        if is_winning_move(board, action, opponent):
            if action == best_action:
                return best_action, "This move blocks the opponent from winning on their next turn."

    # --- Helper: count winning moves after a move (fork detection) ---
    def count_winning_moves(board, p):
        count = 0
        for action in actions(board):
            if is_winning_move(board, action, p):
                count += 1
        return count

    # --- 3. Create fork ---
    new_board = result(board, best_action)
    if count_winning_moves(new_board, current) >= 2:
        return best_action, "This move creates a fork, giving multiple ways to win."

    # --- 4. Block opponent fork ---
    for action in actions(board):
        new_board = result(board, action)
        if count_winning_moves(new_board, opponent) >= 2:
            if action == best_action:
                return best_action, "This move blocks the opponent from creating a fork."

    # --- 5. Minimax explanation ---
    score = None
    if current == X:
        score = max(
            min_value(result(board, action)) for action in actions(board)
        )
    else:
        score = min(
            max_value(result(board, action)) for action in actions(board)
        )

    if score == 1:
        return best_action, "This move leads to a guaranteed win with optimal play."
    elif score == 0:
        return best_action, "This move ensures a draw with optimal play."
    else:
        return best_action, "All moves lead to a loss, but this delays defeat as much as possible."
    
