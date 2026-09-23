"""
Main driver script for the Command-Line Interface (CLI) Tic Tac Toe game.
Orchestrates turn management, game state evaluation, and replay sessions
using modular OOP components (Board, Player, ComputerPlayer).
"""

from board import Board
from computerplayer import ComputerPlayer
from player import Player

print("🎮 Welcome to Tic Tac Toe! 🎮")

# Prompt user for player name (defaults to 'Player 1' if left empty)
player_name = input("Enter your name: ").strip() or "Player 1"
human_player = Player(name=player_name, symbol="x")
computer_player = ComputerPlayer(symbol="o")

game_on = True

# Main outer loop managing repeated game sessions
while game_on:
    # Instantiate and display a clean board for the new round
    board = Board()
    board.display_board()

    # Round loop handling alternating turns
    while True:
        # 1. Human player turn execution
        human_player.make_move(board)

        # Check win or draw conditions following human move
        if board.check_win():
            print("* " * 30 + f"\n🏆 The Winner is {human_player.name}! 🏆\n" + "* " * 30)
            break
        elif len(board.position_list) == 9:
            print("* " * 30 + "\nIt's a Draw!\n" + "* " * 30)
            break

        # 2. Computer AI turn execution
        computer_player.make_move(board)

        # Check win or draw conditions following computer move
        if board.check_win():
            print("* " * 30 + f"\n🏆 The Winner is {computer_player.name}! 🏆\n" + "* " * 30)
            break
        elif len(board.position_list) == 9:
            print("* " * 30 + "\nIt's a Draw!\n" + "* " * 30)
            break

    # Replay query after round completion
    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again != 'y':
        print(f"\nThanks for playing {human_player.name}!")
        game_on = False