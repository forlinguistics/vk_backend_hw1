"""TicTac game"""
import re


class TicTacGame:
    """TicTac game class"""
    reference = """
     1 2 3
    a | |
     -+-+-
    b | |
     -+-+-
    c | |
    """
    player_switch = True
    row_dict = {'A': 0, 'B': 1, 'C': 2}

    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]

    def show_board(self):
        """prints current board state"""
        print('\n-+-+-\n'.join(['|'.join(row) for row in self.board]))

    def validate_input(self, inp):
        """validates user input and changes the board state if it is correct"""
        move_pattern = re.compile('[A-C] [1-3]')
        if not move_pattern.match(inp):
            raise ValueError(r'Input should have the valid format(Example "A 2")')
        row, col = inp.split()
        row = self.row_dict[row]
        col = int(col) - 1
        if self.board[row][col] != ' ':
            raise ValueError('Field is not empty')
        if self.player_switch:
            self.board[row][col] = 'x'
        else:
            self.board[row][col] = 'o'
        self.player_switch = not self.player_switch
        return True

    def check_winner(self):
        """checks winner from current board state"""
        for i in range(3):
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True, self.board[i][0]

            if self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True, self.board[0][i]

        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True, self.board[0][0]

        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True, self.board[0][2]

        return False, ' '

    def start_game(self):
        """game method"""
        move_cnt = 0
        print("Game started: to make a move enter position coordinates (reference below).")
        print(self.reference)
        while True:
            while True:
                try:
                    print("Make a move: ")
                    move = input()
                    self.validate_input(move)
                    break
                except ValueError as err:
                    print(err)
            self.show_board()
            winner = self.check_winner()
            if winner[0]:
                return f'Game ended. Winner is {winner[1]}'
            move_cnt += 1
            if move_cnt == 9:
                return 'Game ended. Draw'


if __name__ == '__main__':
    game = TicTacGame()
    print(game.start_game())
