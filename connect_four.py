# Initialize Player1 and Player2 symbols
player_symbol = 'X'
player_symbol_real = [' ', 'X', '0']

# Create column labels
numbers = [i for i in range(1, 8)]
column_label = list()
for number in numbers:
    column_label.append([' ' * 2, str(number), ' '])
column_output = ''
for item in column_label:
    column_output += ''.join(item)
print(column_output)

# Initialize the character structure of the container
top_edge = ['+', '-' * 3]
non_interactable_row = ['|', ' ' * 3]
interactable_row = ['|', ' ', player_symbol, ' ']

# Create the lid of the container
lid_structure = list()
for _ in range(1, 8):
    lid_structure.append(top_edge)
lid_structure_output = ''
for item in lid_structure:
    lid_structure_output += ''.join(item)
# Add the last element to the lid structure
lid_structure_output += '+'

# print(lid_structure_output)

# Create the side of the container
side_structure = list()
for _ in range(1, 8):
    side_structure.append(non_interactable_row)
side_structure_output = ''
for item in side_structure:
    side_structure_output += ''.join(item)
# Add the last element to the side structure
side_structure_output += '|'
# print(side_structure_output)

# Create the row containing the location of X and O
side_structure_interact = list()
for _ in range(1, 8):
    side_structure_interact.append(interactable_row)
side_structure_interact_output = ''
for item in side_structure_interact:
    side_structure_interact_output += ''.join(item)
# Add the last element to the side structure
side_structure_interact_output += '|'

# Iterate 6x for lids to create the structure of the board
for _ in range(1, 7):
    print(lid_structure_output)
    print(side_structure_output)
    print(side_structure_interact_output)
    print(side_structure_output)
print(lid_structure_output)


