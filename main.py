import sys
import math
from random import randrange


class Tictactoe:
    def __init__(self, size, ai=True):
        self.size = size
        self.board = self.create_board(self.size)
        sys.setrecursionlimit(3**(self.size**2))
        self.ai = ai

    @staticmethod
    def print_board(board):
        for i in board:
            ret = list(map(lambda a: str(a).zfill(len(str(len(board) ** 2 - 1))), i))
            print(ret)

    def play_game(self):
        turn_counter = 0
        players = ["X", "O"]

        if self.ai:
            # ai_player = players[randrange(2)]
            ai_player = players[0]
            print(f"AI plays {ai_player}")

        while not self.get_result(self.board) and turn_counter < self.size ** 2:
            current_player = players[turn_counter % 2]

            while True:
                Tictactoe.print_board(self.board)
                print("\n\n")
                try:
                    if self.ai and ai_player == current_player:
                        cell_input = self.minmaxmove(
                            players[:: (1 if ai_player == 1 else -1)],
                            self.board,
                            0,
                            True,
                        )
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
                except (ValueError, IndexError) as e:
                    print("\nINVALID CELL\n")
                    continue
                break
            turn_counter += 1
        else:
            print("\n\n\n")
            Tictactoe.print_board(self.board)
            winner = Tictactoe.get_result(self.board)
            if winner:
                print(f"\nCongratulations Player {winner}!")
            else:
                print("DRAW!")

    @staticmethod
    def get_result(board):
        size = len(board)
        for i in range(size):
            if all(map(lambda a: a == board[i][0], board[i])):
                return board[i][0]
            column = [x[i] for x in board]
            if all(map(lambda a: a == column[0], column)):
                return column[0]

        diagonal_down = []
        for i in range(size):
            diagonal_down.append(board[i][i])

        if all(map(lambda a: a == diagonal_down[0], diagonal_down)):
            return diagonal_down[0]

        diagonal_up = []
        for i in range(size):
            diagonal_up.append(board[i][size - i - 1])

        if all(map(lambda a: a == diagonal_up[0], diagonal_up)):
            return diagonal_up[0]

        return False

    @staticmethod
    def minmaxmove(players, board, depth, maximize):  # players = [ai_player, player]
        result = Tictactoe.get_result(board)
        if result:
            if result == players[0]:
                return 10 - depth
            elif result == players[1]:
                return -10 + depth
        
        moves = Tictactoe.possible_moves(board)

        if len(moves) == 0:
            print("Draw")
            return 0

        if maximize:
            minmaxscore = -math.inf
            best_move = None
            for i in moves:
                board_copy = Tictactoe.clone_board(board)
                board_row = board_copy[i // len(board_copy)]
                cell_index = board_row.index(i)
                board_row[cell_index] = players[0] # make the move
                score = Tictactoe.minmaxmove(players, board, depth + 1, maximize)
                if score > minmaxscore:
                    minmaxscore = score
                    best_move = i
        elif not maximize:
            minmaxscore = math.inf
            best_move = None
            for i in moves:
                board_copy = Tictactoe.clone_board(board)
                board_row = board_copy[i // len(board_copy)]
                cell_index = board_row.index(i)
                board_row[cell_index] = players[0] # make the move
                score = Tictactoe.minmaxmove(players, board, depth + 1, maximize)
                if score < minmaxscore:
                    minmaxscore = score
                    best_move = i
        if depth == 0:
            return best_move
        else:
            return minmaxscore

    @staticmethod
    def possible_moves(board):
        move_list = []
        for i in board:
            move_list.extend([x for x in i if type(x) == int])
        return move_list

    @staticmethod
    def create_board(size=3):
        board = []
        for i in range(size):
            board.append([None] * size)
            for j in range(size):
                board[i][j] = i * size + j
        return board

    @staticmethod
    def clone_board(board):
        board_clone = []
        for i in board:
            board_clone.append(i.copy())
        return board_clone

game = Tictactoe(3, True)
game.play_game()

input("|Press enter to exit|\t")
