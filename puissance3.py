# PUISSANCE 3
TOKEN_1 = "🟢"
TOKEN_2 = "🟡"
VIDE = "⚫"
N_COLUMNS = 5
N_LINES = 5

tableau = [
    ["⚫", "⚫", "⚫", "⚫", "⚫"],
    ["⚫", "⚫", "⚫", "⚫", "⚫"],
    ["⚫", "⚫", "⚫", "⚫", "⚫"],
    ["⚫", "⚫", "⚫", "⚫", "⚫"],
    ["⚫", "⚫", "⚫", "⚫", "⚫"]
]

winner = None
player = 1

# Token
def get_token(player):
    if player == 1:
        return TOKEN_1
    return TOKEN_2

# Disposition du tableau
def display_grid(tableau):
    for ligne in range(len(tableau)):
        affi = ""
        nbre_colonne = ""

        for colonne in range(len(tableau)):
            affi += f"{tableau[ligne][colonne]}    "
            nbre_colonne += f"     {colonne}"

        print(f"{ligne}   {affi} \n")

    print(f"{nbre_colonne}") 


# Le tour se joue
def play(grid, column, player):
    line = N_LINES - 1

    while grid[line][column] != VIDE and line > -1:
        line -= 1

    if line > -1:
        grid[line][column] = get_token(player)

    return grid

# Check vertical
def check_vertical(grid, column, line):
    if line >= 3:
        return False
    
    if grid[line + 1][column] == grid[line][column] and grid[line + 2][column] == grid[line][column]:
        return True
    return False


# Check vertical
def check_horizontal(grid, column, line):
    if column >= 2:
        if grid[line][column - 1] == grid[line][column] and grid[line][column - 2] == grid[line][column]:
            return True
    if column <= 2:
        if grid[line][column + 1] == grid[line][column] and grid[line][column + 2] == grid[line][column]:
            return True
    if column >= 1 and column <= 3:
        if grid[line][column + 1] == grid[line][column] and grid[line][column - 1] == grid[line][column]:
            return True
    return False

# Check diagonal
def check_diagonalr(grid, column, line):
    if column >= 2 and line >= 2:
        if grid[line - 1][column - 1] == grid[line][column] and grid[line - 2][column - 2] == grid[line][column]:
            return True
    if column <= 2 and line <= 2:
        if grid[line + 1][column + 1] == grid[line][column] and grid[line + 2][column + 2] == grid[line][column]:
            return True
    if column >= 1 and column <= 3 and line >= 1 and line <= 3:
        if grid[line + 1][column + 1] == grid[line][column] and grid[line - 1][column - 1] == grid[line][column]:
            return True
    return False

# Check diagonal
def check_diagonalg(grid, column, line):
    if column <= 2 and line >= 2:
        if grid[line - 1][column + 1] == grid[line][column] and grid[line - 2][column + 2] == grid[line][column]:
            return True
    if column >= 2 and line <= 2:
        if grid[line + 1][column - 1] == grid[line][column] and grid[line + 2][column - 2] == grid[line][column]:
            return True
    if column >= 1 and column <= 3 and line >= 1 and line <= 3:
        if grid[line + 1][column + 1] == grid[line][column] and grid[line - 1][column - 1] == grid[line][column]:
            return True
    return False

# Check si le tableau est complet et pas gagnant
def complet(grid, column, line):
    for value in grid[0]:
        if value == VIDE:
            return False
        
    return True

# Check le gagnant
def check_winner(grid, column, current_player):
    line = 0

    while grid[line][column] == VIDE:
        line += 1

    if check_vertical(grid, column, line) or check_horizontal(grid, column, line) or check_diagonalr(grid, column, line) or check_diagonalg(grid, column, line):
        return True
    return False

while winner == None:
    display_grid(tableau)

    column = input(f"Joueur {get_token(player)} où vas tu jouer ? ")
    column = int(column)

    play(tableau, column, player)

    if check_winner(tableau, column, player):
        winner = player
    else:
        if complet(tableau):
            tableau = [
                ["⚫", "⚫", "⚫", "⚫", "⚫"],
                ["⚫", "⚫", "⚫", "⚫", "⚫"],
                ["⚫", "⚫", "⚫", "⚫", "⚫"],
                ["⚫", "⚫", "⚫", "⚫", "⚫"],
                ["⚫", "⚫", "⚫", "⚫", "⚫"]
            ]
        if player == 1:
            player = 2
        else:
            player = 1

display_grid(tableau)
print(f"Whow joueur {get_token(winner)}, tu as gagné!")