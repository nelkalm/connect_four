# Initialize Player1 and Player2 symbols
player_symbol = ' '
player_symbol_real = [' ', 'X', '0']
num_columns = 7
num_rows = 6
numbers = [i for i in range(1, num_columns + 1)]


# Create column labels
def create_column_labels(num_columns):
    numbers = [i for i in range(1, num_columns + 1)]
    column_label = list()
    for number in numbers:
        column_label.append([' ' * 2, str(number), ' '])
    column_output = ''
    for item in column_label:
        column_output += ''.join(item)
    print(column_output)


# Create container structures
def create_container_structure(character_structure_list, num_columns):
    created_structure = list()
    for _ in range(1, num_columns + 1):
        created_structure.append(character_structure_list)
    created_structure_output = ''
    for item in created_structure:
        created_structure_output += ''.join(item)
    created_structure_output += character_structure_list[0]
    print(created_structure_output)


# Initialize the character structure of the container
top_edge = ['+', '-' * 3]
non_interactable_row = ['|', ' ' * 3]
interactable_row = ['|', ' ', player_symbol, ' ']


# Create Board:
def create_board(top_edge, non_interactable_row, interactable_row, num_columns):
    # Create board
    for _ in range(1, num_columns):
        create_container_structure(top_edge, num_columns)
        create_container_structure(non_interactable_row, num_columns)
        create_container_structure(interactable_row, num_columns)
        create_container_structure(non_interactable_row, num_columns)
    create_container_structure(top_edge, num_columns)


# Create a non-outputting board in the back-end
# Example:
# [
#     [[], [], [], [], [], [], []],
#     [[], [], [], [], [], [], []],
#     [[], [], [], [], [], [], []],
#     [[], [], [], [], [], [], []],
#     [[], [], [], [], [], [], []],
#     [[], [], [], [], [], [], []],
# ]
def create_nonoutput(num_columns, num_rows):
    board = list()
    for i in range(1, num_rows + 1):
        board.append([])
    for row in board:
        for i in range(1, num_columns + 1):
            row.append([])
    return board


current_board = create_nonoutput(num_columns, num_rows)


def play_piece(column_choice, player_piece, board):
    row_number = len(board)

    # Check if the column is full:
    if player_piece == board[0][column_choice - 1]:
        print(f'Trying to place an {player_piece} in column {column_choice}')
        print(f'Make sure to pick a column between 1 and 7 that is not full')
    else:
        for row in range(row_number - 1, -1, -1):
            if not board[row][column_choice - 1]:
                board[row][column_choice - 1] = player_piece
                print(f"Placed an {player_piece} in column {row}")
                break
            else:
                continue
    return board


# Playing a player piece in column
player_column_choice = 5
player_piece_choice = 'W'
print("Trying to place an " + player_piece_choice + " in column " + str(player_column_choice))
if player_column_choice not in numbers:
    print("Make sure to pick a column between 1 and " + str(num_columns) + " that is not full")
if player_piece_choice not in player_symbol_real:
    print("Make sure to use either an 'X' or an 'O' as your piece")
else:
    print(f"Placed an {player_piece_choice} in column {player_column_choice}")
print()
create_column_labels(num_columns)
create_board(top_edge, non_interactable_row, interactable_row, num_columns)

# print(create_nonoutput(7, 6))
print(current_board)
# print(play_piece(5, 'X', current_board))
# print(play_piece(5, 'X', current_board))
# print(play_piece(5, '0', current_board))
# print(play_piece(5, 'X', current_board))
# print(play_piece(5, 'X', current_board))
# print(play_piece(5, 'X', current_board))
# print(play_piece(5, 'X', current_board))
# print(play_piece(5, 'X', current_board))
