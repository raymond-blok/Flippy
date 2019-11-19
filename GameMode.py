from GameRule import *

class GameMode:
    def __init__(self, gameRules):
        # Save a list of GameRules.
        self.gameRules = gameRules
        # Keep the total score
        self.score = 0
        # Somehow get access to list of components
        #??????

    # Create a method to check the list with GameRules.
    def checkRules(self, sensor):
        for gameRule in self.gameRules:
            if(gameRule.getSensor() == sensor):
                self.checkAndAddScore(gameRule)
                self.checkSpecialCase(gameRule)
                return gameRule.getRelayElement()

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