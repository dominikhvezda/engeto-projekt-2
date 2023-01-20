"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Dominik Hvězda
email: domik.hvezduj@gmail.com
discord: domino#0624
"""

lines = 40 * "="
line = 40 * "-"
rules = """GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row"""

# úvodní pozdrav, pravidla hry
print(
        "Welcome to Tic Tac Toe",
        lines,
        rules,
        lines,
        "Let's start the game:",
        line,
        sep="\n"
)

# hrací pole - místo "|" příjde "X" nebo "O" v průběhu hry
board = []
for i in range(3):
    board.append(["|","|","|"])

# hrací plocha
def print_board():
    print("+---+---+---+")
    for row in board:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print("+---+---+---+")

# zjistit, jestli je konec hry
def check_game_over():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "|":
            return True, board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "|":
            return True, board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "|":
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "|":
        return True, board[0][2]
    my_list = []
    for sub_list in board:
        my_list.extend(sub_list)
    if "|" not in my_list:
        return True, "Tie"
    return False, None

# samotná hra
player = "X"
while True:
    print_board()
    print(lines)
    print("Player {} | Please enter your move number:".format(player),
          end=" ")
    move = input()
    print(lines)
    if not move.isdigit():
      print("Invalid input. Please enter a number between 1 and 9.")
      continue
    move = int(move)
    if move not in range(1, 10):
        print("Invalid input. Please enter a number between 1 and 9.")
        continue
    row = (move - 1) // 3
    col = (move - 1) % 3
    if board[row][col] != "|":
        print("Place already filled. Please choose another.")
        continue
    board[row][col] = player
    game_over, winner = check_game_over()
    if game_over:
        print_board()
        if winner == "Tie":
            print("Game over. It's a tie.")
        else:
            print("Congratulations, the player {} WON!".format(winner))
        break
    player = "X" if player == "O" else 'O'