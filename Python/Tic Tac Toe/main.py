BOARD_SIZE = 3

board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

player = "X"

while True:
    print("   " + "  ".join(str(i) for i in range(BOARD_SIZE)))
    for i in range(BOARD_SIZE):
        print(f"{i}  {' | '.join(board[i])}")
        if i < BOARD_SIZE - 1:
            print("  " + "-" * (BOARD_SIZE * 4 - 1))
      
    winner = None
    for i in range(BOARD_SIZE):
        if board[i][0] != " " and all(board[i][j] == board[i][0] for j in range(BOARD_SIZE)):
            winner = board[i][0]
        if board[0][i] != " " and all(board[j][i] == board[0][i] for j in range(BOARD_SIZE)):
            winner = board[0][i]
    if board[0][0] != " " and all(board[i][i] == board[0][0] for i in range(BOARD_SIZE)):
        winner = board[0][0]
    if board[0][BOARD_SIZE - 1] != " " and all(board[i][BOARD_SIZE - i - 1] == board[0][BOARD_SIZE - 1] for i in range(BOARD_SIZE)):
        winner = board[0][BOARD_SIZE - 1]
    if winner is not None:
        print(f"Congratulations! {winner} wins!")
        break
    elif all(board[i][j] != " " for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
        print("It's a tie!")
        break

    while True:
        move = input(f"Player {player}, enter your move (row column): ")
        try:
            row, col = [int(i) for i in move.split()]
        except ValueError:
            print("Invalid input. Enter row and column separated by a space.")
            continue
        if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
            print(f"Invalid move. Row and column must be between 0 and {BOARD_SIZE - 1}.")
            continue
        if board[row][col] != " ":
            print("Invalid move. That space is already occupied.")
            continue
        break

    board[row][col] = player

    player = "O" if player == "X" else "X"
