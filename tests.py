import unittest
from unittest.mock import patch

import paper_scissor_rock


class TestGame(unittest.TestCase):

    def setUp(self):
        self.options = {'rock': 0, 'paper': 1, 'scissors': 2}
        self.game = paper_scissor_rock.RockPaperScissors()
        self.test_dict = {
            "ties": 0,
            "wins": 0,
            "losses": 0,
        }

    def tearDown(self):
        del self.game

    def test_random_choice(self):
        """
        :return: True if choice is in options keys
        """
        choice = self.game.random_choice()
        self.assertIn(choice, list(self.options.keys()))

    def test_random_wrong_choice_str(self):
        """
        :return: True if choice is not in options keys
        """
        choice = 'dog'
        self.assertNotIn(choice, list(self.options.keys()))

    def test_random_wrong_choice_int(self):
        """
        :return: True if choice is not in options keys
        """
        choice = 1
        self.assertNotIn(choice, list(self.options.keys()))

    def test_check_result_player1_wins(self):
        """
        :return: True if check_result function returns dict like {"ties": 0, "wins": 1, "losses": 0}
        """
        player1 = self.options['scissors']
        dict_test = self.test_dict.copy()
        self.assertDictEqual(dict_test, self.test_dict)

        result = self.game.check_result(player1, dict_test)
        self.assertEqual(self.options['scissors'], player1)
        self.assertIn(player1, list(self.options.values()))
        self.assertDictEqual(result, {"ties": 0, "wins": 1, "losses": 0})

    def test_check_result_player1_lose(self):
        """
        :return: True if check_result function returns dict like {"ties": 0, "wins": 0, "losses": 1}
        """
        player1 = self.options['rock']
        dict_test = self.test_dict.copy()
        self.assertDictEqual(dict_test, self.test_dict)

        result = self.game.check_result(player1, dict_test)
        self.assertEqual(self.options['rock'], player1)
        self.assertIn(player1, list(self.options.values()))
        self.assertDictEqual(result, {"ties": 0, "wins": 0, "losses": 1})

    def test_check_result_player1_ties(self):
        """
        :return: True if check_result function returns dict like {"ties": 100, "wins": 0, "losses": 0}
        """
        player1 = self.options['paper']
        dict_test = self.test_dict.copy()
        self.assertDictEqual(dict_test, self.test_dict)

        result = self.game.check_result(player1, dict_test)
        self.assertIn(player1, list(self.options.values()))
        self.assertDictEqual(result, {"ties": 1, "wins": 0, "losses": 0})

    def test_play_ngames_player1_wins(self):
        """
        :return: True if player1 wins 100 times and dict like {"ties": 0, "wins": 100, "losses": 0}
        """
        player1 = self.options["scissors"]
        random_pl1 = False
        n = 100
        result = self.game.play_ngames(n, random_pl1, player1)

        self.assertEqual(self.options['scissors'], player1)
        self.assertIn(player1, list(self.options.values()))
        self.assertDictEqual(result, {"ties": 0, "wins": 100, "losses": 0})

    def test_play_ngames_player1_losses(self):
        """
        :return: True if player1 losses 100 times and dict like {"ties": 0, "wins": 0, "losses": 100}
        """
        player1 = self.options['rock']
        random_pl1 = False
        n = 100
        result = self.game.play_ngames(n, random_pl1, player1)

        self.assertEqual(self.options['rock'], player1)
        self.assertIn(player1, list(self.options.values()))
        self.assertDictEqual(result, {"ties": 0, "wins": 0, "losses": 100})

    def test_play_ngames_player1_ties(self):
        """
        :return: True if player1 ties 100 times and dict like {"ties": 100, "wins": 0, "losses": 0}
        """
        player1 = self.options['paper']
        random_pl1 = False
        n = 100
        result = self.game.play_ngames(n, random_pl1, player1)

        self.assertEqual(self.options['paper'], player1)
        self.assertIn(player1, list(self.options.values()))
        self.assertDictEqual(result, {"ties": 100, "wins": 0, "losses": 0})


if __name__ == '__main__':
    unittest.main()
