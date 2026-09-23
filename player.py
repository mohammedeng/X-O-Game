


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


    def make_move(self, board):
        """تاخذ اسم اللاعب ورمز اللعب وتتحقق من صحة الحركة"""
        while True:
            raw_input = input(f"\n{self.name} ({self.symbol})\nEnter the number: ")

            if not raw_input.isdigit():
                print("Invalid input! Please enter a number.")
                continue

            position = int(raw_input) - 1

            if position < 0 or position > 8:
                print("Position must be between 1 and 9.")
                continue

            if position in board.position_list:
                print(f"Position {position + 1} is already taken.")
                continue

            board.position_list.append(position)
            board.board_list[position] = self.symbol
            board.display_board()
            break