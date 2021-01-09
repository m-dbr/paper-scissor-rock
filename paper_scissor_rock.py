import random


def random_choice(options) -> str:
    """
    Chooses a choice randomly from the keys in options.
    :returns: String containing the choice of the computer.
    """
    choices = list(options.keys())
    return random.choice(choices)


def check_result(player1, player2, result_dict) -> dict:
    """
    Check the result of the game: whether player1 wins or loose or ties with computer
    :returns: Dictionary containing the possible results.
    """
    result = (player1 - player2) % 3

    if result == 0:
        result_dict['ties'] += 1
    elif result == 1:
        result_dict['wins'] += 1
    elif result == 2:
        result_dict['losses'] += 1
    return result_dict


def play_ngames(options, player2, n, random_pl1=True, player1=None) -> dict:
    """
    Play n games, check result of each game and update result_dict
    :returns: Dictionary containing the final scores of each n games.
    """
    outcome_dict = {
        "ties": 0,
        "wins": 0,
        "losses": 0,
    }
    result_dict = outcome_dict.copy()

    for i in range(n):
        if random_pl1 is True:
            player1 = options[random_choice(options)]
        check_result(player1, player2, result_dict)

    return result_dict


def print_score(result_dict):
    """
    Print the score of the play depend of data stored in result_dict dictionary.
    """
    print('-------- GAME OVER --------')
    print(f"Player A (computer) wins {result_dict['wins']} times")
    print(f"Player B (paper) wins {result_dict['losses']} times")
    print(f"Tie: {result_dict['ties']} of 100 games")
    print(f"Winner is: {'Player A' if result_dict['wins'] > result_dict['losses'] else 'Player B'}")
    print('--------------------')


def play_again():
    """
    Ask whether player wants to play again or exit the game.
    """
    while True:
        continue_prompt = input('\nDo you wish to play again? (y/n): ').lower()
        if continue_prompt == 'n':
            print("Game is over")
            exit()
        elif continue_prompt == 'y':
            break
        else:
            print("Invalid input!\n")
            continue