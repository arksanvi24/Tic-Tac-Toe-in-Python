import random

def print_grid(grid):
    print("\n".join([" | ".join(row) for row in grid]))
import random

def print_grid(grid):
    print("\n".join([" | ".join(row) for row in grid]))
    print("-" * 9)

def check_winner(grid):
    #rows and columns
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != " ":
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != " ":
            return grid[0][i]

    #diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " ":
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != " ":
        return grid[0][2]

    #draw
    if all(grid[i][j] != " " for i in range(3) for j in range(3)):
        return "Draw"

    return None

def get_empty_positions(grid):
    return [(i, j) for i in range(3) for j in range(3) if grid[i][j] == " "]

def computer_move(grid, symbol):
    empty_positions = get_empty_positions(grid)
    if empty_positions:
        row, col = random.choice(empty_positions)
        grid[row][col] = symbol

def player_move(grid, symbol):
    while True:
        try:
            move = input("Enter your move (row and column, e.g., 1,2): ").split(",")
            row, col = int(move[0]) - 1, int(move[1]) - 1
            if (row, col) in get_empty_positions(grid):
                grid[row][col] = symbol
                break
            else:
                print("Invalid move. The position is already taken or out of bounds.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers between 1 and 3.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    grid = [[" " for _ in range(3)] for _ in range(3)]

    player_symbol = input("Choose your symbol (X or O): ").upper()
    while player_symbol not in ("X", "O"):
        player_symbol = input("Invalid choice. Please choose X or O: ").upper()
    computer_symbol = "O" if player_symbol == "X" else "X"

    print("\nHere's the initial grid:")
    print_grid(grid)

    while True:
        player_move(grid, player_symbol)
        print("\nPlayer's move:")
        print_grid(grid)
        winner = check_winner(grid)
        if winner:
            break

        print("Computer's move...")
        computer_move(grid, computer_symbol)
        print_grid(grid)
        winner = check_winner(grid)
        if winner:
            break

    if winner == "Draw":
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

if __name__ == "__main__":
    main()
