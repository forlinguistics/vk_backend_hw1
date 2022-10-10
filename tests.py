"""TicTac game tests"""
import unittest
import io
from unittest.mock import patch
from main import TicTacGame

EMPTY_OUTP = " | | \n-+-+-\n | | \n-+-+-\n | | \n"
FILLED_OUTP = " |x| \n-+-+-\n | | \n-+-+-\n | | \n"


class TicTacTestCase(unittest.TestCase):
    """TicTac game tests for each method of TicTac game class"""
    win_moves = ['B 1', 'A 1', 'B 2', 'A 2', 'B 3']
    draw_moves = ['A 1', 'B 2', 'A 2', 'A 3', 'C 1', 'C 2', 'C 3', 'B 1', 'B 3']

    def test_validate_inp(self):
        """tests validate_input method"""
        with patch('sys.stdout', new=io.StringIO()) as std_out:
            game = TicTacGame()
            self.assertRaises(ValueError, game.validate_input, 'A.2')
            self.assertRaises(ValueError, game.validate_input, 'A 4')
            self.assertRaises(ValueError, game.validate_input, 'D 2')
            assert game.validate_input('A 2')
            assert game.board[0][1] == 'x'
            self.assertRaises(ValueError, game.validate_input, 'A 2')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_board(self, mock_stdout):
        """test show_board method"""
        game = TicTacGame()
        game.show_board()
        self.assertEqual(mock_stdout.getvalue(), EMPTY_OUTP)
        game.validate_input('A 2')
        game.show_board()
        self.assertEqual(mock_stdout.getvalue(), EMPTY_OUTP + FILLED_OUTP)

    def test_check_winner(self):
        """test check_winner method"""
        with patch('sys.stdout', new=io.StringIO()) as std_out:
            hor_win = ['B 1', 'A 1', 'B 2', 'A 2', 'B 3']
            vert_win = ['A 2', 'A 3', 'B 2', 'B 3', 'C 1', 'C 3']
            diag_win = ['A 3', 'A 1', 'B 2', 'B 1', 'C 1']
            game = TicTacGame()
            for i in hor_win:
                game.validate_input(i)
            assert (game.check_winner() == (True, 'x'))
            game = TicTacGame()
            for i in vert_win:
                game.validate_input(i)
            game.show_board()
            assert (game.check_winner() == (True, 'o'))
            game = TicTacGame()
            for i in diag_win:
                game.validate_input(i)
            assert (game.check_winner() == (True, 'x'))
            game = TicTacGame()
            game.validate_input('B 2')
            assert (game.check_winner() == (False, ' '))

    @patch('builtins.input', side_effect=win_moves)
    def test_start_game_win(self, mock_inputs):
        """test start_game method with first player win scenario"""
        with patch('sys.stdout', new=io.StringIO()) as std_out:
            game = TicTacGame()
            assert game.start_game() == 'Game ended. Winner is x'

    @patch('builtins.input', side_effect=draw_moves)
    def test_start_game_draw(self, mock_inputs):
        """test start_game method with draw scenario"""
        with patch('sys.stdout', new=io.StringIO()) as std_out:
            game = TicTacGame()
            assert game.start_game() == 'Game ended. Draw'
