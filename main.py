from random import randrange

class Tictactoe:
    def __init__(self, size, ai=True):
        self.size = size
        self.board = self.create_board(self.size)
        self.ai = ai

    def print_board(self):
        for i in self.board:
            ret = list(map(lambda a: str(a).zfill(len(str(self.size ** 2 - 1))), i))
            print(ret)

    def play_game(self):
        turn_counter = 0
        players = ["X", "O"]
        
        if self.ai:
            ai_player = players[randrange(2)]

        print(f"AI plays {ai_player}")

        while not self.get_result():
            current_player = players[turn_counter % 2]

            while True:
                self.print_board()
                print("\n\n")
                try:
                    if self.ai and ai_player == current_player:
                        cell_input = self.minmaxmove()
                    else:
                        cell_input = int(
                            input(
                                f"Type which cell to place in (Player {current_player}): "
                            )
                        )
                    board_row = self.board[int(cell_input) // self.size]
                    cell_index = board_row.index(cell_input)
                    if board_row[cell_index] is not int:
                        assert ValueError
                    board_row[cell_index] = current_player
                except ValueError:
                    print("\nINVALID CELL\n")
                    continue
                break
            turn_counter += 1
        else:
            print("\n\n\n")
            self.print_board()
            print(f"\nCongratulations Player {players[(turn_counter-1)%2]}!")

    def get_result(self):
        for i in range(self.size):
            if all(map(lambda a: a == self.board[i][0], self.board[i])):
                return self.board[i][0]
            column = [x[i] for x in self.board]
            if all(map(lambda a: a == column[0], column)):
                return column[0]
        
        diagonal_down = []
        for i in range(self.size):
            diagonal_down.append(self.board[i][i])
        
        if all(map(lambda a: a == diagonal_down[0], diagonal_down)):
            return diagonal_down[0]
        
        diagonal_up = []
        for i in range(self.size):
            diagonal_up.append(self.board[i][self.size-i-1])
        
        if all(map(lambda a: a == diagonal_up[0], diagonal_up)):
            return diagonal_up[0]
        return False

    def minmaxmove(self):
        return randrange(self.size**2)

    @staticmethod
    def create_board(size=3):
        board = []
        for i in range(size):
            board.append([None] * size)
            for j in range(size):
                board[i][j] = i * size + j
        return board


game = Tictactoe(3)
game.play_game()
