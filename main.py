import paper_scissor_rock

if __name__ == "__main__":
    options = {'rock': 0, 'paper': 1, 'scissors': 2}
    player2 = options['paper']
    # random_pl1 when True: player1 is randomly chosen, when False player1 have to bo set
    random_pl1 = True
    n = 100

    while True:
        game = paper_scissor_rock.play_ngames(options, player2, n, random_pl1)
        paper_scissor_rock.print_score(game)
        paper_scissor_rock.play_again()









