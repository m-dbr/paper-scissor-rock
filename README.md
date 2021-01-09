# Paper-Scissor-Rock console game
This is a simple Paper-Scissor-Rock console game. The main goal was to play **n** games with computer with only one choice (player choose to use **paper** through all **n** games).

## Getting started
### Prerequisites
* **python3** installed

### Clone repository
In order to download game, clone this repository to chosen directory on your local system:
```
$ git clone git@github.com:m-dbr/paper-scissor-rock.git
```

## Usage
### Play a game
In order to play a game, navigate to catalog with source code and type:
```
$ python3 main.py
```

default values:
* player2 chose only paper,
* player1 (computer) randomly chose other possibilites,
* number of games: 100.

The output of the game should looks like:

```
-------- GAME OVER --------
Player A (computer) wins 33 times
Player B (paper) wins 31 times
Tie: 36 of 100 games
Winner is: Player A
--------------------

Do you wish to play again? (y,n):
```

by choosing **y** at the end, the game will start over again. By choosing **n**, program ends.

### Test code with unittest
Simple unittests were written to test Paper-Scissor-Rock console game code.
In order to run unittests type:

```
python3 -m unittest tests.TestGame
```

##### list of tests:
* tests whether _random_choice_ function works correctly:
    * _test_random_wrong_choice_ 
    * _test_random_wrong_choice_str_
    * _test_random_wrong_choice_int_
* tests whether _check_result_ function works correctly:
    * _test_check_result_player1_wins_
    * _test_check_result_player1_losses_
    * _test_check_result_player1_ties_
* tests whether _play_ngames_ function works correctly:
    * ???

