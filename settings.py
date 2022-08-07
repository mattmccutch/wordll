__author__ = "Lech Szymanski"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "lech.szymanski@otago.ac.nz"
__date__ = "July 2022"

# You can manipulate these settings to change how the game is played.

game_settings = {

    # name of the agent file (replace with my_agent.py when your agent is ready)
    "agentFile": "my_agent.py",

    # 'english' or  'francais' or 'deutsch' or 'italiano' or 'espanol'
    "dictionary": 'english',

    "wordLength": 5,

    "numberOfGuesses": 6,  # number of guesses per game

    "numberOfGames": 100,  # total number of games played

    "mode": 'hard',  # 'easy' or 'hard'

    "repeats": True,  # whether the words are allowed to repeat or not

    "verbose": True,

    "seed": 0   # seed for random choices of words in the game, None for random seed

}
