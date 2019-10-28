from GameMode import *
from GameRule import *

class Game(object):

    def __init__(self):
        gameRules = []
        gameRules.append(GameRule("LBUTTON", "Lflipper", 10, None))
        gameRules.append(GameRule("RBUTTON", "Rflipper", 10, None))
        gameRules.append(GameRule("RESET", None, 10, "ENDGAME"))
        self.gameMode = GameMode(gameRules)
        while(True):
            sensor = input()
            response = self.gameMode.checkRules(sensor)
            print(response)
            print(self.gameMode.score)

Game()
