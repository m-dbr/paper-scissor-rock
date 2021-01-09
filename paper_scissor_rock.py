import random


class RockPaperScissors:
    """
    Class to handle an instance of a Rock-Paper-Scissors game
    with n rounds.
    """

    def __init__(self) -> None:
        """
        Initialize the variables for the class
        """
        self.options = {'rock': 0, 'paper': 1, 'scissors': 2}
        self.player2 = self.options['paper']
        self.outcome_dict = {
            "ties": 0,
            "wins": 0,
            "losses": 0,
        }

    def random_choice(self) -> str:
        """
        Chooses a choice randomly from the keys in options.
        :returns: String containing the choice of the computer.
        """
        choices = list(self.options.keys())
        return random.choice(choices)

    def check_result(self, player1: int, result_dict: dict) -> dict:
        """
        Check the result of the game: whether player1 wins or loose or ties with computer
        :returns: Dictionary containing the possible results.
        """
        result = (player1 - self.player2) % 3

        if result == 0:
            result_dict['ties'] += 1
        elif result == 1:
            result_dict['wins'] += 1
        elif result == 2:
            result_dict['losses'] += 1
        return result_dict

    def print_score(self, result_dict: dict) -> None:
        """
        Print the score of the play depending of the data stored in result_dict dictionary.
        """
        print('-------- GAME OVER --------')
        print(f"Player A (computer) wins {result_dict['wins']} times")
        print(f"Player B (player paper) wins {result_dict['losses']} times")
        print(f"Tie: {result_dict['ties']} of 100 games")
        print(f"Winner is: {'Player A' if result_dict['wins'] > result_dict['losses'] else 'Player B'}")
        print('--------------------')

    def play_ngames(self, n=100, random_pl1=True, player1=None) -> dict:
        """
        Play n games, check result of each game and update result_dict
        :returns: Dictionary containing the final scores of each n games.
        """
        result_dict_updated = self.outcome_dict.copy()

        for i in range(n):
            if random_pl1 is True:
                player1 = self.options[self.random_choice()]
            self.check_result(player1, result_dict_updated)

        return result_dict_updated