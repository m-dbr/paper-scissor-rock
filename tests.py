import unittest
import paper_scissor_rock


class TestGame(unittest.TestCase):

    def setUp(self):
        self.options = {'rock': 0, 'paper': 1, 'scissors': 2}
        self.test_dict = {
            "ties": 0,
            "wins": 0,
            "losses": 0,
        }

    def test_random_choice(self):
        choice = paper_scissor_rock.random_choice(self.options)
        self.assertIn(choice, list(self.options.keys()))

    def test_random_wrong_choice_str(self):
        choice = 'dog'
        self.assertNotIn(choice, list(self.options.keys()))

    def test_random_wrong_choice_int(self):
        choice = 1
        self.assertNotIn(choice, list(self.options.keys()))

    # def test_check_result_player1_wins(self):
    #     player1 = self.options['scissors']
    #     player2 = self.options['paper']
    #     dict_test = self.test_dict.copy()
    #     result = main.check_result(player1, player2, dict_test)
    #
    #     self.assertIn('scissors', list(self.options.keys()))
    #     self.assertIn('paper', list(self.options.keys()))
    #     self.assertEqual(self.options['scissors'], player1)
    #     self.assertEqual(self.options['paper'], player2)
    #     self.assertIn(player1, list(self.options.values()))
    #     self.assertIn(player2, list(self.options.values()))
    #     self.assertDictEqual(result, {"ties": 0, "wins": 1, "losses": 0}, msg='Wrong dictionary content: should be wins: 1')
    #     self.assertEqual(len(result), 3)

    # def test_check_result_player1_lose(self):
    #     player1 = self.options['rock']
    #     player2 = self.options['paper']
    #     dict_test = self.test_dict.copy()
    #     result = main.check_result(player1, player2, dict_test)
    #
    #     self.assertIn('rock', list(self.options.keys()))
    #     self.assertIn('paper', list(self.options.keys()))
    #     self.assertEqual(self.options['rock'], player1)
    #     self.assertEqual(self.options['paper'], player2)
    #     self.assertIn(player1, list(self.options.values()))
    #     self.assertIn(player2, list(self.options.values()))
    #     self.assertDictEqual(result, {"ties": 0, "wins": 0, "losses": 1}, msg='Wrong dictionary content: should be losses: 1')
    #     self.assertEqual(result['losses'], 1)
    #     self.assertEqual(len(result), 3)
    #
    # def test_check_result_player1_ties(self):
    #     player1 = self.options['paper']
    #     player2 = self.options['paper']
    #     dict_test = self.test_dict.copy()
    #     result = main.check_result(player1, player2, dict_test)
    #
    #     self.assertIn('paper', list(self.options.keys()))
    #     self.assertEqual(self.options['paper'], player2)
    #     self.assertIn(player1, list(self.options.values()))
    #     self.assertIn(player2, list(self.options.values()))
    #     self.assertDictEqual(result, {"ties": 1, "wins": 0, "losses": 0}, msg='Wrong dictionary content: should be losses: 1')
    #     self.assertEqual(len(result), 3)
    #
    # def test_play_ngames_player1_wins(self):
    #     player1 = self.options['scissors']
    #     player2 = self.options['paper']
    #     n = 100
    #     random_pl1 = False
    #     result = main.play_ngames(self.options, player2, n, random_pl1, player1)
    #
    #     self.assertDictEqual(result, {"ties": 0, "wins": 100, "losses": 0})
    #
    # def test_play_ngames_player1_looses(self):
    #     player1 = self.options['rock']
    #     player2 = self.options['paper']
    #     n = 100
    #     random_pl1 = False
    #     result = main.play_ngames(self.options, player2, n, random_pl1, player1)
    #
    #     self.assertDictEqual(result, {"ties": 0, "wins": 0, "losses": 100})
    #
    # def test_play_ngames_player1_ties(self):
    #     player1 = self.options['paper']
    #     player2 = self.options['paper']
    #     n = 100
    #     random_pl1 = False
    #     result = main.play_ngames(self.options, player2, n, random_pl1, player1)
    #
    #     self.assertDictEqual(result, {"ties": 100, "wins": 0, "losses": 0})



if __name__ == '__main__':
    unittest.main()