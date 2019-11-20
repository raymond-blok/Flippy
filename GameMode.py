from GameRule import *

class GameMode:
    def __init__(self, gameRules):
        # Save a list of GameRules.
        self.gameRules = gameRules
        # Keep the total score
        self.score = 0

    # Create a method to check the list with GameRules.
    def checkRules(self, activeSensorElements):
        triggeredRelayElements = []
        for gameRule in self.gameRules:
            check = False
            for activeSensorElement in activeSensorElements:
                if(gameRule.getSensor() == activeSensorElement):
                    check = True
                    success = gameRule.activate()
                    if(success):
                        if(gameRule.triggered == False):
                            self.checkAndAddScore(gameRule)
                            self.checkSpecialCase(gameRule)
                            gameRule.triggered = True
                        relayElement = gameRule.getRelayElement()
                        if(relayElement != None):
                            triggeredRelayElements.append(relayElement)
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
