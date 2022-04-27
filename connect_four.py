# Initialize Player1 and Player2 symbols
player_symbol = 'X'
player_symbol_real = [' ', 'X', '0']
num_columns = 7


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

# Create column labels
create_column_labels(num_columns)

# Iterate 6x for lids to create the structure of the board
for _ in range(1, num_columns):
    create_container_structure(top_edge, num_columns)
    create_container_structure(non_interactable_row, num_columns)
    create_container_structure(interactable_row, num_columns)
    create_container_structure(non_interactable_row, num_columns)
create_container_structure(top_edge, num_columns)


