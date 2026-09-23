from random import choice, randint
from Gui.player import Player

# All 8 possible index triplets that result in a winning line
WINNING_COMPOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical Columns
    (0, 4, 8), (2, 4, 6)               # Diagonal Lines
]

# 0-indexed corner positions on the 3x3 board
ANGELS = (0, 2, 6, 8)


class ComputerPlayer(Player):
    """
    Represents an AI-controlled computer player inheriting from the Player class.
    Uses a rule-based decision hierarchy (Win, Block, Strategic Positioning, Center Control, Fallback).
    """

    def __init__(self, symbol: str = "o") -> None:
        """
        Initializes the ComputerPlayer with default name 'computer'.

        Args:
            symbol (str): Assigned mark for the computer player ('o' by default).
        """
        super().__init__(name="computer", symbol=symbol)

    def make_move(self, board) -> None:
        """
        Evaluates the current board state and executes the optimal computer move based on:
        1. Winning condition check (completes 3-in-a-row for computer).
        2. Blocking condition check (blocks opponent's potential 3-in-a-row).
        3. Strategic positioning (prioritizes setup lines and corner spots).
        4. Center priority (takes center index 4 early in the game).
        5. Fallback random selection.

        Args:
            board (Board): The active Board instance managing game state.
        """
        while True:
            computer_position = None

            # Rule 1: Win - Check if computer can complete a winning line
            for a, b, c in WINNING_COMPOS:
                if (board.board_list[a] == "o" and board.board_list[b] == "o") and (board.board_list[c] not in ("x", "o")):
                    computer_position = c
                    break
                elif (board.board_list[a] == "o" and board.board_list[c] == "o") and (board.board_list[b] not in ("x", "o")):
                    computer_position = b
                    break
                elif (board.board_list[b] == "o" and board.board_list[c] == "o") and (board.board_list[a] not in ("x", "o")):
                    computer_position = a
                    break

            # Rule 2: Block - Check if opponent is about to win and block them
            else:
                for a, b, c in WINNING_COMPOS:
                    if (board.board_list[a] == "x" and board.board_list[b] == "x") and (board.board_list[c] not in ("x", "o")):
                        computer_position = c
                        break
                    elif board.board_list[a] == "x" and board.board_list[c] == "x" and (board.board_list[b] not in ("x", "o")):
                        computer_position = b
                        break
                    elif board.board_list[b] == "x" and board.board_list[c] == "x" and (board.board_list[a] not in ("x", "o")):
                        computer_position = a
                        break

                # Rule 3: Strategic Positioning - Look for open opportunities near existing marks
                else:
                    empty_spots = []
                    angel_spots = []
                    for a, b, c in WINNING_COMPOS:
                        if board.board_list[a] == "o" and (board.board_list[b] not in ("x", "o")) and (board.board_list[c] not in ("x", "o")):
                            empty_spots.extend([b, c])
                        elif board.board_list[b] == "o" and (board.board_list[a] not in ("x", "o")) and (board.board_list[c] not in ("x", "o")):
                            empty_spots.extend([a, c])
                        elif board.board_list[c] == "o" and (board.board_list[b] not in ("x", "o")) and (board.board_list[a] not in ("x", "o")):
                            empty_spots.extend([b, a])

                    if empty_spots:
                        # Prioritize corner spots if available
                        for spot in empty_spots:
                            if spot in ANGELS:
                                angel_spots.append(spot)
                                empty_spots.remove(spot)

                        if angel_spots:
                            computer_position = choice(angel_spots)
                        else:
                            computer_position = choice(empty_spots)

            # Rule 4: Center Priority - Take center square (index 4) early in game if available
            if len(board.position_list) <= 1 and (board.board_list[4] != "o" and board.board_list[4] != "x"):
                computer_position = 4
            # Rule 5: Fallback - Select random position if no strategic rule triggered
            elif computer_position is None:
                computer_position = randint(0, 8)

            # Validate selected move is available and update state
            if computer_position not in board.position_list:
                board.position_list.append(computer_position)
                board.board_list[computer_position] = self.symbol
                # board.display_board()
                break