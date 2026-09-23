#Local 2-Player Mode or Human vs. Human (PvP):
# Two human players share the same keyboard and take alternating turns on one screen.
# ANSI escape codes for terminal text formatting
RED = "\033[91m"    # Red text for symbol 'X'
BLUE = "\033[94m"   # Blue text for symbol 'O'
RESET = "\033[0m"   # Resets text formatting to terminal default


def get_colored_symbol(val: str) -> str:
    """
    Applies ANSI color formatting to 'X' and 'O' symbols for terminal output.

    Args:
        val (str): The current value at a board position (number or symbol).

    Returns:
        str: Formatted colored string for 'X' or 'O', or the raw string if unassigned.
    """
    if val.upper() == 'X':
        return f"{RED}X{RESET}"
    elif val.upper() == 'O':
        return f"{BLUE}O{RESET}"
    return val


def display_board(b: list) -> None:
    """
    Renders the current 3x3 game board grid to the terminal screen.

    Args:
        b (list): A list of 9 elements representing the board state.
    """
    # Create a temporary list of colored values exclusively for visual rendering
    colored_b = [get_colored_symbol(item) for item in b]

    print("\n")
    print(f"        {colored_b[0]} | {colored_b[1]} | {colored_b[2]} ")
    print("       ---+---+---")
    print(f"        {colored_b[3]} | {colored_b[4]} | {colored_b[5]} ")
    print("       ---+---+---")
    print(f"        {colored_b[6]} | {colored_b[7]} | {colored_b[8]} ")
    print("\n")


# All 8 possible index triplets that result in a winning line
WINNING_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical Columns
    (0, 4, 8), (2, 4, 6)               # Diagonal Lines
]


def check_win(b: list) -> bool:
    """
    Evaluates whether the current board state contains any winning combination.

    Args:
        b (list): The list representing board grid entries.

    Returns:
        bool: True if three identical symbols line up in a winning pattern, False otherwise.
    """
    return any(b[a] == b[b_idx] == b[c] for a, b_idx, c in WINNING_COMBOS)


def player(player_name: str, value: str, position_list: list) -> None:
    """
    Prompts the active player for position input, validates the choice, and updates the board.

    Args:
        player_name (str): Name of the player making the move.
        value (str): Player's symbol ('x' or 'o').
        position_list (list): Tracks positions that have already been selected.
    """
    while True:
        raw_input = input(f"\n{player_name} ({value})\nEnter the number: ")

        # Validate that the entry is numeric
        if not raw_input.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        position = int(raw_input)

        # Validate that the chosen position falls within board limits
        if position < 1 or position > 9:
            print("Position must be between 1 and 9.")
            continue

        # Check if the square has already been chosen
        if position in position_list:
            print(f"Position {position} is already taken.")
            continue

        # Record position, place mark on board, and re-render grid
        position_list.append(position)
        board[position - 1] = value
        display_board(board)
        break


# Prompt player names once at startup (assign default names if left empty)
player1_name = input("Enter Player 1 name (X): ").strip() or "Player 1"
player2_name = input("Enter Player 2 name (O): ").strip() or "Player 2"

game_on = True

# Main game outer loop
while game_on:
    # Initialize a clean board and position tracker for each round
    board = ['1', '2', '3',
             '4', '5', '6',
             '7', '8', '9']
    position_list = []

    display_board(board)

    # Round loop
    while True:
        # Player 1 turn execution
        player(player_name=player1_name, value="x", position_list=position_list)
        if check_win(board):
            print("* " * 30 + f"\n🏆 The Winner is {player1_name}! 🏆\n" + "* " * 30)
            break
        elif len(position_list) == 9:
            print("* " * 30 + "\nIt's a Draw!\n" + "* " * 30)
            break

        # Player 2 turn execution
        player(player_name=player2_name, value="o", position_list=position_list)
        if check_win(board):
            print("* " * 30 + f"\n🏆 The Winner is {player2_name}! 🏆\n" + "* " * 30)
            break
        elif len(position_list) == 9:
            print("* " * 30 + "\nIt's a Draw!\n" + "* " * 30)
            break

    # Replay query after round completion
    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again != 'y':
        print(f"\nThanks for playing {player1_name} and {player2_name}!")
        game_on = False







