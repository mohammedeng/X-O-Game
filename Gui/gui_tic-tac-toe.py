"""
CustomTkinter Graphical User Interface (GUI) for Tic Tac Toe.
Connects modular game backend classes (Board, Player, ComputerPlayer)
with an interactive desktop application window.
"""

import customtkinter as ctk
from board import Board
from computerplayer import ComputerPlayer
from player import Player

# 1. Configure GUI theme and visual appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# 2. Initialize main application window
window = ctk.CTk()
window.title("Tic Tac Toe")
window.geometry("360x520")
window.resizable(width=False, height=False)

# 3. Instantiate game logic backend objects
board = Board()
human = Player(name="Player 1", symbol="x")
computer = ComputerPlayer(symbol="o")

# 4. Initialize status display label
status_label = ctk.CTkLabel(
    master=window,
    text=f"{human.name}'s Turn (X)",
    font=("Arial", 22, "bold")
)
status_label.pack(pady=20)


def check_game_over(player) -> bool:
    """
    Checks if the active player has won or if the game ended in a draw.
    Disables remaining interactive buttons when a terminal state is reached.

    Args:
        player: The player object (Player or ComputerPlayer) who just moved.

    Returns:
        bool: True if the game has concluded, False if play continues.
    """
    if board.check_win():
        status_label.configure(text=f"🏆 {player.name} Wins!")
        # Disable button clicks across the grid once the game ends
        for btn in buttons:
            btn.configure(command=None)
        return True
    elif len(board.position_list) == 9:
        status_label.configure(text="🤝 It's a Draw!")
        return True
    return False


def computer_turn() -> None:
    """
    Executes the computer AI turn, updates the corresponding GUI grid button,
    and checks for win/draw status transitions.
    """
    # Record initial position list count to verify new move execution
    prev_count = len(board.position_list)

    # Call backend AI to update board array
    computer.make_move(board)

    # Determine index chosen by computer and update button appearance
    if len(board.position_list) > prev_count:
        chosen_index = board.position_list[-1]
        buttons[chosen_index].configure(
            text=computer.symbol.upper(),
            text_color="#000000",  # Dark color for symbol 'O'
            command=None
        )

    # Evaluate game completion; if active, hand turn back to human player
    if not check_game_over(computer):
        status_label.configure(text=f"{human.name}'s Turn (X)")


def on_button_click(index: int) -> None:
    """
    Handles human player button click events, updates backend board state,
    and schedules computer AI response turn.

    Args:
        index (int): 0-indexed position corresponding to the clicked grid button.
    """
    # Prevent action if position was previously selected
    if index in board.position_list:
        return

    # Update backend position tracking and board state
    board.position_list.append(index)
    board.board_list[index] = human.symbol
    buttons[index].configure(
        text=human.symbol.upper(),
        text_color="#FF4444",  # Bright red for symbol 'X'
        command=None
    )

    # Evaluate status; schedule computer AI response after short delay if active
    if not check_game_over(human):
        status_label.configure(text=f"{computer.name}'s Turn (O)")
        window.after(400, computer_turn)  # 400ms delay for realistic turn response


def reset_game() -> None:
    """
    Resets backend board instance, clears button visual states, and resets status label.
    """
    global board
    board = Board()  # Create a clean backend board instance
    status_label.configure(text=f"{human.name}'s Turn (X)")

    # Reset grid buttons to default numbers and click commands
    for i, btn in enumerate(buttons):
        btn.configure(
            text=f"{i + 1}",
            text_color="#FFFFFF",
            command=lambda idx=i: on_button_click(idx)
        )


# 5. Create container frame for 3x3 grid layout
grid_frame = ctk.CTkFrame(master=window)
grid_frame.pack(pady=20, padx=20)

# 6. Instantiate 3x3 grid of board buttons
buttons = []
for i in range(9):
    row, col = divmod(i, 3)  # Map index 0-8 to row/column 2D grid coordinates
    btn = ctk.CTkButton(
        master=grid_frame,
        text=f"{i + 1}",
        width=80,
        height=80,
        font=("Arial", 44),
        command=lambda index=i: on_button_click(index),
    )
    btn.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(btn)

# 7. Create restart control button at bottom of window
restart_btn = ctk.CTkButton(
    master=window,
    text="Restart Game 🔄",
    font=("Arial", 16, "bold"),
    fg_color="#2B2B2B",
    hover_color="#3A3A3A",
    command=reset_game
)
restart_btn.pack(pady=20)

# 8. Start application event loop
window.mainloop()