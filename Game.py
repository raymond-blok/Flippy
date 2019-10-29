from GameMode import *
from GameRule import *
from HardWare import *

class Game(object):

    def __init__(self):
        gameRules = []
        gameRules.append(GameRule(65, 66, 10, None))
        self.gameMode = GameMode(gameRules)
        self.hardWare = HardWare()
        while(True):
            triggeredRelayElements = []
            activeSensorElements = self.hardWare.checkSensorElements()
            if(len(activeSensorElements) > 0):
                for activeSensorElement in activeSensorElements:
                    response = self.gameMode.checkRules(activeSensorElement)
                    if(response != None):
                        triggeredRelayElements.append(response)
            self.hardWare.activateRelayElements(triggeredRelayElements)





Game()
