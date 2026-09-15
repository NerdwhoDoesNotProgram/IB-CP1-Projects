# IB, 2nd period - Tic Tac Toe game for the Pseudocode assignemnt

def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c]:
            return board[a]

    if all(space == "X" or space == "O" for space in board):
        return "tie"

    return None


def player_turn(board, player):
    while True:
        choice = int(input(f"Player {player}, choose a space (0-8): "))

        if choice < 0 or choice > 8:
            print("Please choose a number from 0 to 8.")
        elif board[choice] in ["X", "O"]:
            print("That space is already taken.")
        else:
            board[choice] = player
            break


def play_game():
    board = ["0", "1", "2",
             "3", "4", "5",
             "6", "7", "8"]
    player = "X"

    display_board(board)

    while True:
        player_turn(board, player)
        display_board(board)

        result = check_winner(board)

        if result == "X":
            print("Player X wins!")
            break
        elif result == "O":
            print("Player O wins!")
            break
        elif result == "tie":
            print("It's a tie!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"


play_game()