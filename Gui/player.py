
class Player:
    """
    Represents a human player in the Tic Tac Toe game.

    Attributes:
        name (str): The display name of the player.
        symbol (str): The mark assigned to the player (e.g., 'X' or 'O').
    """

    def __init__(self, name: str, symbol: str) -> None:
        """
        Initializes a new Player instance.

        Args:
            name (str): The name of the player.
            symbol (str): The player's assigned symbol ('X' or 'O').
        """
        self.name = name
        self.symbol = symbol

    def make_move(self, board) -> None:
        """
        Prompts the player for input, validates the choice, and updates the board state.

        Args:
            board (Board): The active Board object managing grid state and rendering.
        """
        while True:
            raw_input = input(f"\n{self.name} ({self.symbol})\nEnter the number: ")

            # Validate that the input consists of numeric digits
            if not raw_input.isdigit():
                print("Invalid input! Please enter a number.")
                continue

            # Convert 1-indexed user input (1-9) to 0-indexed list index (0-8)
            position = int(raw_input) - 1

            # Validate that the move is within board boundaries
            if position < 0 or position > 8:
                print("Position must be between 1 and 9.")
                continue

            # Check if the chosen square has already been selected
            if position in board.position_list:
                print(f"Position {position + 1} is already taken.")
                continue

            # Record position, update board grid state, and refresh visual display
            board.position_list.append(position)
            board.board_list[position] = self.symbol
            # board.display_board()
            break
