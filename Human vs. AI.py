from random import choice, randint

# ANSI escape codes for terminal text formatting
RED = "\033[91m"    # Red text for symbol 'X'
BLUE = "\033[94m"   # Blue text for symbol 'O'
RESET = "\033[0m"   # Resets text formatting to terminal default

# Tuple containing 0-indexed corner positions on the board (Top-Left, Top-Right, Bottom-Left, Bottom-Right)
ANGELS = (0, 2, 6, 8)


def get_colored_symbol(val: str) -> str:
    """
    Applies ANSI color formatting to 'X' and 'O' symbols for terminal output.

    Args:
        val (str): The current value at a board position (number or symbol).

    Returns:
        str: Formatted colored string for 'X' or 'O', or the raw string if unassigned.
    """
    if str(val).upper() == 'X':
        return f"{RED}X{RESET}"
    elif str(val).upper() == 'O':
        return f"{BLUE}O{RESET}"
    return str(val)


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
WINNING_COMPOS = [
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
    return any(b[a] == b[b_idx] == b[c] for a, b_idx, c in WINNING_COMPOS)


def player(player_name: str, value: str, position_list: list) -> None:
    """
    Prompts the human player for input, validates the choice, and updates the board.

    Args:
        player_name (str): Name of the player making the move.
        value (str): Player's symbol ('x' or 'o').
        position_list (list): Tracks 0-indexed positions that have already been chosen.
    """
    while True:
        raw_input = input(f"\n{player_name} ({value})\nEnter the number: ")

        # Validate numeric entry
        if not raw_input.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        position = int(raw_input) - 1  # Convert 1-9 user input to 0-8 list index

        # Validate boundaries
        if position < 0 or position > 8:
            print("Position must be between 1 and 9.")
            continue

        # Check if square is taken
        if position in position_list:
            print(f"Position {position + 1} is already taken.")
            continue

        # Update move state and render board
        position_list.append(position)
        board[position] = value
        display_board(board)
        break


def computer_player(position_list: list) -> None:
    """
    Executes the computer AI turn using a rule-based decision hierarchy:
    1. Winning condition check (completes 3-in-a-row for 'O').
    2. Blocking condition check (blocks human 2-in-a-row for 'X').
    3. Strategic move selection (prioritizes corners/center).
    4. Fallback random selection.

    Args:
        position_list (list): Tracks 0-indexed positions that have already been chosen.
    """

    while True:
        computer_position = None

        # Rule 1: Win - Check if computer can complete a 3-in-a-row sequence
        for a, b, c in WINNING_COMPOS:
            if (board[a] == "o" and board[b] == "o") and (board[c] not in ("x", "o")):
                computer_position = c
                break
            elif (board[a] == "o" and board[c] == "o") and (board[b] not in ("x", "o")):
                computer_position = b
                break
            elif (board[b] == "o" and board[c] == "o") and (board[a] not in ("x", "o")):
                computer_position = a
                break

        # Rule 2: Block - If no winning move, block opponent's potential 3-in-a-row
        else:
            for a, b, c in WINNING_COMPOS:
                if (board[a] == "x" and board[b] == "x") and (board[c] not in ("x", "o")):
                    computer_position = c
                    break
                elif board[a] == "x" and board[c] == "x" and (board[b] not in ("x", "o")):
                    computer_position = b
                    break
                elif board[b] == "x" and board[c] == "x" and (board[a] not in ("x", "o")):
                    computer_position = a
                    break
            else:
                # Rule 3: Strategic Positioning - Look for open opportunities near existing marks
                empty_spots = []
                angel_spots = []

                for a, b, c in WINNING_COMPOS:
                    if board[a] == "o" and (board[b] not in ("x", "o")) and (
                            board[c] not in ("x", "o")):
                        empty_spots.append(b)
                        empty_spots.append(c)

                    elif board[b] == "o" and (board[a] not in ("x", "o")) and (
                            board[c] not in ("x", "o")):
                        # empty_spots = [a, c]
                        empty_spots.append(a)
                        empty_spots.append(c)

                    elif board[c] == "o" and (board[b] not in ("x", "o")) and (
                            board[a] not in ("x", "o")):

                        empty_spots.append(b)
                        empty_spots.append(a)


                if empty_spots:

                    for spot in empty_spots:
                        # Prioritize corners if available
                        if spot in ANGELS:
                            angel_spots.append(spot)
                            empty_spots.remove(spot)
                    if angel_spots:

                        computer_position = choice(angel_spots)
                    else:
                        computer_position = choice(empty_spots)


        # Rule 4: Center Priority - Take the center square (index 4) early in the game if available
        if len(position_list) <= 1 and (board[4] != "o" and board[4] != "x"):
            computer_position = 4
        # Rule 5: Fallback - Pick a completely random position if no heuristic triggered
        elif computer_position is None:
            computer_position = randint(0, 8)

        # Validate that the chosen position is not taken
        if computer_position not in position_list:
            position_list.append(computer_position)
            board[computer_position] = 'o'
            display_board(board)
            break


# Prompt player name at startup (assign default name if left empty)
player1_name = input("Enter Player 1 name (X): ").strip() or "Player 1"

game_on = True

# Main game outer loop
while game_on:
    # Initialize board grid with 1-indexed integers and clean move tracker
    board = [1, 2, 3,
             4, 5, 6,
             7, 8, 9]
    position_list = []

    display_board(board)

    # Round execution loop
    while True:
        # Human player turn
        player(player_name=player1_name, value="x", position_list=position_list)
        if check_win(board):
            print("* " * 30 + f"\n🏆 The Winner is {player1_name}! 🏆\n" + "* " * 30)
            break
        elif len(position_list) == 9:
            print("* " * 30 + "\nIt's a Draw!\n" + "* " * 30)
            break

        # Computer AI turn
        computer_player(position_list=position_list)
        if check_win(board):
            print("* " * 30 + f"\n🏆 The Winner is computer! 🏆\n" + "* " * 30)
            break
        elif len(position_list) == 9:
            print("* " * 30 + "\nIt's a Draw!\n" + "* " * 30)
            break

    # Replay query after round completion
    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again != 'y':
        print(f"\nThanks for playing {player1_name}!")
        game_on = False