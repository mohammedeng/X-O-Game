# The 8 possible index combinations that complete a winning line
WINNING_COMPOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical Columns
    (0, 4, 8), (2, 4, 6)               # Diagonal Lines
]

# ANSI escape codes for colored terminal output
RED = "\033[91m"    # Red color formatting for symbol 'X'
BLUE = "\033[94m"   # Blue color formatting for symbol 'O'
RESET = "\033[0m"   # Resets terminal formatting to default
ANGELS = (0, 2, 6, 8)  # Corner positions on the 3x3 grid


class Board:
    """
    Manages the 3x3 Tic-Tac-Toe grid state, position tracking,
    terminal formatting, and win condition evaluation.
    """

    def __init__(self) -> None:
        """
        Initializes the board grid with numbers 1 through 9
        and sets up an empty list to track selected position indices.
        """
        self.board_list = [i for i in range(1, 10)]
        self.position_list = []

    def get_colored_symbol(self, val: str) -> str:
        """
        Applies ANSI color codes to player symbols ('X' / 'O') for terminal output
        without modifying the underlying board state values.

        Args:
            val (str): The value present at a board spot (number or symbol).

        Returns:
            str: The ANSI color-formatted string for terminal rendering.
        """
        if val.upper() == 'X':
            return f"{RED}X{RESET}"
        elif val.upper() == 'O':
            return f"{BLUE}O{RESET}"
        return val

    def display_board(self) -> None:
        """
        Renders the current 3x3 grid layout in the terminal with colored player marks.
        """
        # Generate a colored list representation exclusively for display
        colored_b = [self.get_colored_symbol(str(item)) for item in self.board_list]

        print("\n")
        print(f"        {colored_b[0]} | {colored_b[1]} | {colored_b[2]} ")
        print("       ---+---+---")
        print(f"        {colored_b[3]} | {colored_b[4]} | {colored_b[5]} ")
        print("       ---+---+---")
        print(f"        {colored_b[6]} | {colored_b[7]} | {colored_b[8]} ")
        print("\n")

    def check_win(self) -> bool:
        """
        Evaluates the board state against all possible winning combinations.

        Returns:
            bool: True if 3 identical symbols form a line across any winning combination,
                  False otherwise.
        """
        return any(
            self.board_list[a] == self.board_list[b_idx] == self.board_list[c]
            for a, b_idx, c in WINNING_COMPOS
        )