from copy import deepcopy


def print_10x10_matrix(matrix):
    horizontal_line = "+---" * 10 + "+"

    print(horizontal_line)
    for i in range(10):
        for j in range(10):
            print("| {} ".format(matrix[i][j]), end="")
        print("|")
        print(horizontal_line)


def has_won(board, symbol):
    count = 0

    # Check horizontally and vertically
    for i in range(10):
        for j in range(8):
            if board[i][j] == symbol == board[i][j+1] == board[i][j+2]:
                count += 1  # Horizontal
            if board[j][i] == symbol == board[j+1][i] == board[j+2][i]:
                count += 1  # Vertical

    # Check diagonally (top-left to bottom-right)
    for i in range(8):
        for j in range(8):
            if board[i][j] == symbol == board[i+1][j+1] == board[i+2][j+2]:
                count += 1

    # Check diagonally (top-right to bottom-left)
    for i in range(8):
        for j in range(2, 10):
            if board[i][j] == symbol == board[i+1][j-1] == board[i+2][j-2]:
                count += 1

    return count

def evaluate_board(board):

    x = has_won(board, "X")
    y = has_won(board, "O")
    if x > y:
        return 1
    if y > x:
        return -1
    else:
        x_count = 0
        y_count = 0
        for i in range(4, 7):
            for j in range(4, 7):
                if board[i][j] == "X":
                    x_count+=1
                if board[i][j] == "O":
                    y_count+=1
        return x_count - y_count

def has_won(board, symbol):
    count = 0

    # Check horizontally and vertically
    for i in range(10):
        for j in range(8):
            if board[i][j] == symbol == board[i][j+1] == board[i][j+2]:
                count += 1  # Horizontal
            if board[j][i] == symbol == board[j+1][i] == board[j+2][i]:
                count += 1  # Vertical

    # Check diagonally (top-left to bottom-right)
    for i in range(8):
        for j in range(8):
            if board[i][j] == symbol == board[i+1][j+1] == board[i+2][j+2]:
                count += 1

    # Check diagonally (top-right to bottom-left)
    for i in range(8):
        for j in range(2, 10):
            if board[i][j] == symbol == board[i+1][j-1] == board[i+2][j-2]:
                count += 1

    return count

def select_space(board, move, turn):
    if move not in range(1, 101):
        return False
    row = int((move - 1) / 10)
    if row == 0:
        col = (move - 1)
    else:
        col = (move-(11*row)+row-1)
    if board[row][col] != "X" and board[row][col] != "O":
        board[row][col] = turn
        return True
    else:
        return False


def game_is_over(board):
    return len(available_moves(board)) == 0


def available_moves(board):
    moves = []
    for row in board:
        for col in row:
            if col != "X" and col != "O":
                moves.append(int(col))
    return moves

def minimax(input_board, is_maximizing, depth, alpha , beta):
    # Base case - the game is over, so we return the value of the board
    if game_is_over(input_board) or depth == 0:
        return [evaluate_board(input_board)]
    best_move = ""
    if is_maximizing == True:
        best_value = -float("Inf")
        symbol = "X"
    else:
        best_value = float("Inf")
        symbol = "O"
    for move in available_moves(input_board):
        new_board = deepcopy(input_board)
        select_space(new_board, move, symbol)
        hypothetical_value = minimax(new_board, not is_maximizing, depth - 1, alpha, beta)[0]
        if is_maximizing == True and hypothetical_value > best_value:
            best_value = hypothetical_value
            best_move = move
            alpha = max(alpha, best_value)
        if is_maximizing == False and hypothetical_value < best_value:
            best_value = hypothetical_value
            best_move = move
            beta = min(beta, best_value)
        if alpha >= beta:
            break
    return [best_value, best_move, alpha, beta]

# Example usage:
board = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
    ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
    ['31', '32', '33', '34', '35', '36', '37', '38', '39', '40'],
    ['41', '42', '43', '44', '45', '46', '47', '48', '49', '50'],
    ['51', '52', '53', '54', '55', '56', '57', '58', '59', '60'],
    ['61', '62', '63', '64', '65', '66', '67', '68', '69', '70'],
    ['71', '72', '73', '74', '75', '76', '77', '78', '79', '80'],
    ['81', '82', '83', '84', '85', '86', '87', '88', '89', '90'],
    ['91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
]


while not game_is_over(board):
    # opponent_row, opponent_col = [int(i) for i in input().split()]
    # if opponent_row == 0:
    #     move = ((opponent_row*10)+1) + (opponent_col+1) - 1
    # else:
    #     move = opponent_col+(11*opponent_row)-opponent_row+1
    move = minimax(board, False, 2, -float("Inf"), float("Inf"))[1]
    select_space(board, move , "O")

    if not game_is_over(board):
        my_move = minimax(board, True, 1, -float("Inf"), float("Inf"))[1]
        row = int((my_move - 1) / 10)
        if row == 0:
            col = (my_move - 1)
        else:
            col = (my_move - (11 * row) + row - 1)
        select_space(board, my_move, "X")
        print(row, col)
    print_10x10_matrix(board)
if game_is_over(board):
    X = has_won(board, "X")
    Y = has_won(board, "O")
    print("The x:" + str(X))
    print("The o:" + str(Y))