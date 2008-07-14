__author__ = 'Tom Schaul, tom@idsia.ch'

from pybrain.rl import Agent
from pybrain.rl.environments.twoplayergames import GomokuGame


class GomokuPlayer(Agent):
    """ a class of agent that can play the capture game, i.e. provides actions in the format:
    (playerid, position)
    playerid is self.color, by convention. 
    It generally also has access to the game object. """
    def __init__(self, game, color = GomokuGame.BLACK, **args):
        self.game = game
        self.color = color
        self.setArgs(**args)
    
    