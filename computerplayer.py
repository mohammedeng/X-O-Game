from player import Player
from random import randint,choice
WINNING_COMPOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # الصفوف (Rows)
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # الأعمدة (Columns)
    (0, 4, 8), (2, 4, 6)               # الأقطار (Diagonals)
]

ANGELS =(0,2,6,8)

class ComputerPlayer(Player):
    def __init__(self, symbol="o"):
        super().__init__( name="computer",symbol=symbol)


    def make_move(self, board):

        while True:
            computer_position = None

            for a, b, c in WINNING_COMPOS:

                if (board.board_list[a] == "o" and board.board_list[b] == "o") and (board.board_list[c] not in ("x", "o")):
                    print("wining condtion 2 c =", c)
                    computer_position = c
                    break
                elif (board.board_list[a] == "o" and board.board_list[c] == "o") and (board.board_list[b] not in ("x", "o")):
                    print("wining condtion 3 b =", b)

                    computer_position = b
                    break
                elif (board.board_list[b] == "o" and board.board_list[c] == "o") and (board.board_list[a] not in ("x", "o")):
                    print("wining condtion 4 a =", a)

                    computer_position = a
                    break
                # Block the player: If the player has 2-in-a-row with an empty spot,
                # pick that spot to block them.
            else:
                for a, b, c in WINNING_COMPOS:
                    if (board.board_list[a] == "x" and board.board_list[b] == "x") and (board.board_list[c] not in ("x", "o")):
                        print("rows=", (a, b, c))
                        print("block condition 1", 'c=', c)
                        computer_position = c
                        break

                    elif board.board_list[a] == "x" and board.board_list[c] == "x" and (board.board_list[b] not in ("x", "o")):
                        print("rows=", (a, b, c))
                        print("block condition 2", 'b=', b)

                        computer_position = b
                        break

                    elif board.board_list[b] == "x" and board.board_list[c] == "x" and (board.board_list[a] not in ("x", "o")):
                        print("rows=", (a, b, c))

                        print("block condition 3", 'a=', a)

                        computer_position = a
                        break

                else:
                    empty_spots = []
                    angel_spots = []
                    for a, b, c in WINNING_COMPOS:
                        if board.board_list[a] == "o" and (board.board_list[b] not in ("x", "o")) and (board.board_list[c] not in ("x", "o")):
                            empty_spots.append(b)
                            empty_spots.append(c)

                        elif board.board_list[b] == "o" and (board.board_list[a] not in ("x", "o")) and (board.board_list[c] not in ("x", "o")):
                            # empty_spots = [a, c]
                            empty_spots.append(a)
                            empty_spots.append(c)

                        elif board.board_list[c] == "o" and (board.board_list[b] not in ("x", "o")) and (board.board_list[a] not in ("x", "o")):
                            # empty_spots = [b, a]
                            empty_spots.append(b)
                            empty_spots.append(a)

                    print("empty_spots", empty_spots)
                    if empty_spots :
                        # if (empty_spots[0] in ANGELS and empty_spots[1] in ANGELS) or (
                        #         empty_spots[0] not in ANGELS and empty_spots[1] not in ANGELS):
                        #     computer_position = choice(empty_spots)
                        for spot in empty_spots:
                            if spot in ANGELS:
                                angel_spots.append(spot)
                                empty_spots.remove(spot)
                        if angel_spots :
                            computer_position = choice(angel_spots)
                        else:
                            computer_position =choice(empty_spots)


                        # else:
                        #     for spot in empty_spots:
                        #         if spot in ANGELS:
                        #             computer_position = spot

            if len(board.position_list) <= 1 and (board.board_list[4] != "o" and board.board_list[4] != "x"):
                computer_position = 4
            elif computer_position is None:
                computer_position = randint(0, 8)

            if computer_position not in board.position_list:
                print("computer condtion 2 ,computer postion is :", computer_position)
                board.position_list.append(computer_position)
                print("computer postion", computer_position)
                board.board_list[computer_position] = self.symbol
                board.display_board()
                break

