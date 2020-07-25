class Tictactoe:
    def __init__(self, size):
        self.board = self.create_board(size)

    def play_game(self, ai = False):
        pass

    def print_board(self):
        for i in self.board:
            ret = list(map(lambda a: str(a).zfill(len(str(len(self.board) ** 2 -1))), i))
            print(ret)

    @staticmethod
    def create_board(size=3):
        board = []
        for i in range(size):
            board.append([None] * size)
            for j in range(size):
                board[i][j] = i * size + j
        return board


game = Tictactoe(3)
game.print_board()
