
from copy import deepcopy


def print_boards(boards):

    mess = f"""
    |-------------|   |-------------|   |-------------|
    | Tic Tac Toe |   | Tic Tac Toe |   | Tic Tac Toe |
    |-------------|   |-------------|   |-------------|
    |             |   |             |   |             |
    |    {boards[0][0][0]} {boards[0][0][1]} {boards[0][0][2]}    |   |    {boards[1][0][0]} {boards[1][0][1]} {boards[1][0][2]}    |   |    {boards[2][0][0]} {boards[2][0][1]} {boards[2][0][2]}    |
    |    {boards[0][1][0]} {boards[0][1][1]} {boards[0][1][2]}    |   |    {boards[1][1][0]} {boards[1][1][1]} {boards[1][1][2]}    |   |    {boards[2][1][0]} {boards[2][1][1]} {boards[2][1][2]}    |
    |    {boards[0][2][0]} {boards[0][2][1]} {boards[0][2][2]}    |   |    {boards[1][2][0]} {boards[1][2][1]} {boards[1][2][2]}    |   |    {boards[2][2][0]} {boards[2][2][1]} {boards[2][2][2]}    |
    |             |   |             |   |             |
    |-------------|   |-------------|   |-------------|
    
    |-------------|   |-------------|   |-------------|
    | Tic Tac Toe |   | Tic Tac Toe |   | Tic Tac Toe |
    |-------------|   |-------------|   |-------------|
    |             |   |             |   |             |
    |    {boards[3][0][0]} {boards[3][0][1]} {boards[3][0][2]}    |   |    {boards[4][0][0]} {boards[4][0][1]} {boards[4][0][2]}    |   |    {boards[5][0][0]} {boards[5][0][1]} {boards[5][0][2]}    |
    |    {boards[3][1][0]} {boards[3][1][1]} {boards[3][1][2]}    |   |    {boards[4][1][0]} {boards[4][1][1]} {boards[4][1][2]}    |   |    {boards[5][1][0]} {boards[5][1][1]} {boards[5][1][2]}    |
    |    {boards[3][2][0]} {boards[3][2][1]} {boards[3][2][2]}    |   |    {boards[4][2][0]} {boards[4][2][1]} {boards[4][2][2]}    |   |    {boards[5][2][0]} {boards[5][2][1]} {boards[5][2][2]}    |
    |             |   |             |   |             |
    |-------------|   |-------------|   |-------------|
    
    |-------------|   |-------------|   |-------------|
    | Tic Tac Toe |   | Tic Tac Toe |   | Tic Tac Toe |
    |-------------|   |-------------|   |-------------|
    |             |   |             |   |             |
    |    {boards[6][0][0]} {boards[6][0][1]} {boards[6][0][2]}    |   |    {boards[7][0][0]} {boards[7][0][1]} {boards[7][0][2]}    |   |    {boards[8][0][0]} {boards[8][0][1]} {boards[8][0][2]}    |
    |    {boards[6][1][0]} {boards[6][1][1]} {boards[6][1][2]}    |   |    {boards[7][1][0]} {boards[7][1][1]} {boards[7][1][2]}    |   |    {boards[8][1][0]} {boards[8][1][1]} {boards[8][1][2]}    |
    |    {boards[6][2][0]} {boards[6][2][1]} {boards[6][2][2]}    |   |    {boards[7][2][0]} {boards[7][2][1]} {boards[7][2][2]}    |   |    {boards[8][2][0]} {boards[8][2][1]} {boards[8][2][2]}    |
    |             |   |             |   |             |
    |-------------|   |-------------|   |-------------|
    
    """
    print(mess)



def print_board(board):
    mess = """
    |-------------|
    | Tic Tac Toe |
    |-------------|
    |             |
    |    {} {} {}    |
    |    {} {} {}    |
    |    {} {} {}    |
    |             |
    |-------------|
    """.format(board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2])
    print(mess)


def evaluate_big_board(board):
    x_count = 0
    y_count = 0
    for x in my_board:
        for y in x:
            if y == "X":
                x_count += 1
            if y == "O":
                y_count += 1
    if len(available_moves(board)) == 0:
        if x_count > y_count:
            return 1
        if y_count > x_count:
            return -1
        else:
            return 0
    else:
        if has_won(board, "X"):
            return 1
        if has_won(board, "O"):
            return -1


def evaluate_board(board):
    if has_won(board, "X"):
        return 1
    if has_won(board, "O"):
        return -1
    else:
        return 0


def available_moves(board):
    moves = []
    for row in board:
        for col in row:
            if col != "X" and col != "O":
                moves.append(int(col))
    return moves


def has_won(board, symbol):
    for row in board:
        if row.count(symbol) == 3:
            return True
    for i in range(3):
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False


def select_space(board, move, turn):
    if move not in range(1, 10):
        return False
    row = int((move - 1) / 3)
    col = (move - 1) % 3
    if board[row][col] != "X" and board[row][col] != "O":
        board[row][col] = turn
        return True
    else:
        return False


def game_is_over(board):
    return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0


def minimax(input_board, is_maximizing, depth):
    # Base case - the game is over, so we return the value of the board
    if game_is_over(input_board) or depth == 0:
        return [evaluate_board(input_board)]
    best_move = ""
    if is_maximizing:
        best_value = -float("Inf")
        symbol = "X"
    else:
        best_value = float("Inf")
        symbol = "O"
    for move in available_moves(input_board):
        new_board = deepcopy(input_board)
        select_space(new_board, move, symbol)
        hypothetical_value = minimax(new_board, not is_maximizing, depth-1)[0]
        if is_maximizing and hypothetical_value > best_value:
            best_value = hypothetical_value
            best_move = move
        if not is_maximizing and hypothetical_value < best_value:
            best_value = hypothetical_value
            best_move = move
    return [best_value, best_move]


my_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]
my_boards = [deepcopy(my_board) for _ in range(0, 9)]
counter = 0
x_move = 0
first = minimax(my_board, False, 5)[1]
while not game_is_over(my_board):
    opponent_row, opponent_col = [int(i) for i in input().split()]
    move = (((opponent_row * 3) + 1) + (opponent_col + 1)) - 1
    if counter == 0:
        select_space(my_boards[first-1], move, "O")
        counter += 1
    else:
        select_space(my_boards[x_move-1], move, "O")

    if not game_is_over(my_board):

        my_move = minimax(my_boards[move-1], True, 5)[1]
        x_move = my_move
        row = int((my_move - 1) / 3)
        col = (my_move - 1) % 3
        select_space(my_boards[move-1], my_move, "X")
        print(row, col)
        print_boards(my_boards)
    for i, x in enumerate(my_boards):
        eval = evaluate_big_board(x)
        if eval == 1:
            row = int((i+1 - 1) / 3)
            col = (i+1 - 1) % 3
            my_board[row][col] = "X"
        if eval == -1:
            row = int((i+1 - 1) / 3)
            col = (i+1 - 1) % 3
            my_board[row][col] = "O"

    print_board(my_board)
