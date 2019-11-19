from GameRule import *
from copy import deepcopy

class GameMode(object):
    def __init__(self, gameRules):
        # Save a list of GameRules.
        self.gameRules = gameRules
        # Keep the total score
        self.score = 0
        #keep track of a list with items to activate in the future.
        self.futureEvents = []
        # Somehow get access to list of components
        #??????

    # Create a method to check the list with GameRules.
    def checkRules(self, activeSensorElements):
        triggeredRelayElements = deepcopy(self.futureEvents)
        self.futureEvents = []
        for gameRule in self.gameRules:
            check = False
            for activeSensorElement in activeSensorElements:
                if(gameRule.getSensor() == activeSensorElement):

                    check = True
                    if(gameRule.triggered == False):
                        success = gameRule.activate()
                        if(success):
                            self.checkAndAddScore(gameRule)
                            self.checkSpecialCase(gameRule)
                            relayElement = gameRule.getRelayElement()
                            if(relayElement != None):
                                triggeredRelayElement.append(relayElement)
                        else:
                            if gameRule in self.futureEvents
                                print("dont")
                            else:
                                self.futureEvents.append(gameRule)
            if(check == False):
                gameRule.deactivate()
        return triggeredRelayElements


    # Create a method to check and add the score.
    def checkAndAddScore(self, gameRule):
        self.score += gameRule.getPoints()

    # Create a method to check special circumstances.
    def checkSpecialCase(self, gameRule):
        case = gameRule.getSpecialCase()
        if(case == None):
            return
        if(case == "ENDGAME"):
            self.endGame()
            return

    # Create a method to end the game.
    def endGame(self):
        self.score = 0

    # Create a method to get the current
