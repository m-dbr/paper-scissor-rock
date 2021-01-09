import paper_scissor_rock

if __name__ == "__main__":

    game = paper_scissor_rock.RockPaperScissors()
    # options needed to RockPaperScissors instance with parameters
    # options = {'rock': 0, 'paper': 1, 'scissors': 2}
    # test_dict = {
    #     "ties": 0,
    #     "wins": 0,
    #     "losses": 0,
    # }
    # player1 = options['scissors']
    while True:
        # Below example of using with player1 fixed
        # game.play_ngames(n=5, random_pl1=False, player1=options["rock"])
        result = game.play_ngames()
        game.print_score(result)
        game.play_again()
