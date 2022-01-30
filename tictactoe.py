import random

X = "X"
O = "O"
EMPTY = "*"

# Bigger board sizes are less likely
RANDOM_SIZES = [3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]

# Type aliases
Player = str
Board = list[list]
Coords = tuple[int, int]


def create_board(size: int) -> Board:
    """
    Create an empty game board.

    :param size: the size of the board
    :return: the initialized board
    """
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(EMPTY)
        board.append(row)
    return board


def check_rows(board, player):
    """"
    Checks the indexes of a row if player won
    """
    for row in board:
        if row.count(player) == len(row):
            return True
    return False


def check_columns(board, player):
    """"
       Checks the indexes of a column if player won
    """
    for i, row in enumerate(board):
        marks = 0
        for j in range(len(row)):
            marks += board[j][i] == player
        if marks == len(row):
            return True
    return False

def check_diagonals(board, player):
    """"
           Checks the indexes of a diagonals if player won
    """
    for i in range(len(board)):
        if board[i][i] != player:
            return False
    return True

def check_diagonals_reverse(board, player):
    """"
               Checks the indexes of a diagonals(other diagonals) if player won
    """
    for i in range(len(board)):
        if board[i][len(board) - i - 1] != player:
            return False
    return True


def won(player: Player, board: Board) -> bool:
    """"
               Checks if a player won (from all directions)
    """
    return check_rows(board, player) or check_columns(board, player) or\
    check_diagonals(board, player) or check_diagonals_reverse(board, player)


def update_board(board: Board, player: Player, coords: Coords):
    """
    Updates a game board with a given player's move.

    :param board: the board to update
    :param player: the player that made the move
    :param coords: the coordinates (row, column) of the player's move
    """
    board[coords[0]][coords[1]] = player


def get_move(player: Player, board) -> Coords:
    """
    Asks a player for their next move.

    :param player: the player whose turn it is to play
    :return: the coordinates the player chose
    """
    n = len(board)
    valid = False
    while not valid:
        row, col = input(f"{player}'s move: ").split()
        if not (row.isdigit() and col.isdigit()):
            print("Not a valid input")
            continue
        row, col = int(row), int(col)
        if (not (0 <= row < n and 0 <= col < n)) or board[row][col] != "*":
            print("Invalid move")
        else:
            valid = True

    return row, col


def show_board(board: Board):
    """
    Print the current state of the game board.

    :param board: the board to display
    """
    for row in board:
        print(" ".join(row))


def show_winner(player: Player):
    """
    Print an endgame message with the name of the winner.

    :param player: the player who won
    """
    print(f"\nAnd the WINNER is: .....\n!!!!!!!!!!!! {player} !!!!!!!!!!!!")


def switch_player(current_player: Player) -> Player:
    """
    Determine whose turn it is next.

    :param current_player: the player who played last
    :return: the player who will play next
    """
    return X if current_player == O else O


def is_tie(board):
    """"
               Checks all fiels are taken (tie)
    """
    count = 0
    for row in board:
        for square in row:
            count += square != '*'
    return True if count == len(board) ** 2 else False


def play_game(board_size: int = None):
    """
    Play a game of Tic-Tac-Toe.

    :param board_size: the size of the game board. randomized by default.
    """
    tie = False

    if not board_size:
        board_size = random.choice(RANDOM_SIZES)
    board = create_board(board_size)
    current_player = O
    while not won(current_player, board):
        if is_tie(board):
            tie = True
            break
        current_player = switch_player(current_player)
        show_board(board)
        coordinates = get_move(current_player, board)
        update_board(board, current_player, coordinates)

    if tie:
        print("It's a tie!")
    else:
        show_winner(current_player)


if __name__ == '__main__':
    play_game()