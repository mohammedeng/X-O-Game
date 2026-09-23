from board import Board
from player import Player
from computerplayer import ComputerPlayer

print("🎮 Welcome to Tic Tac Toe! 🎮")

player_name = input("Enter your name: ").strip() or "Player 1"
human_player = Player(name=player_name, symbol="x")
computer_player = ComputerPlayer(symbol="o")

game_on = True

while game_on:
    # إنشاء لوحة جديدة وتصفيرها مع كل جولة
    board = Board()
    board.display_board()

    while True:
        # 1. دور اللاعب البشري
        human_player.make_move(board)

        if board.check_win():
            print("* " * 30 + f"\n🏆 The Winner is {human_player.name}! 🏆\n" + "* " * 30)
            break
        elif len(board.position_list) == 9:
            print("* " * 30 + "\nIt's a Draw!\n" + "* " * 30)
            break

        # 2. دور الكمبيوتر
        computer_player.make_move(board)

        if board.check_win():
            print("* " * 30 + f"\n🏆 The Winner is {computer_player.name}! 🏆\n" + "* " * 30)
            break
        elif len(board.position_list) == 9:
            print("* " * 30 + "\nIt's a Draw!\n" + "* " * 30)
            break

    # خيار إعادة اللعب
    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again != 'y':
        print(f"\nThanks for playing {human_player.name}!")
        game_on = False