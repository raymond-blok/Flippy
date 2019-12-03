from GameRule import *
import time

class GameMode:
    def __init__(self, gameRules):
        # Save a list of GameRules.
        self.gameRules = gameRules
        # Keep the total score
        self.score = 0
        # list to keep the zone relayList
        self.zoneRelayList = []
        self.delayRelayList = []

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
                            if(gameRule.delay <= 0):
                                triggeredRelayElements.append(relayElement)
                            else:
                                self.addDelayRelay(relayElement, gameRule.delay)

            if(check == False):
                gameRule.deactivate()
        triggeredRelayElements += self.getAndRemoveFinishedRelays()
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
        if(case == "zoneElement"):
            self.zoneRelayList.append(gameRule.relayElement)
            if(len(self.zoneElement) >= 4):
                for zoneRelay in self.zoneRelayList:
                    self.addDelayRelay(zoneRelay, 30)

    # Create a method to end the game.
    def endGame(self):
        self.score = 0

    def checkDelayRelay(self, relay):
        for delayRelay in self.delayRelayList:
            if(delayRelay == relay):
                return False
        return True
    def addDelayRelay(self, relay, delay):
        if(self.checkDelayRelay(relay)):
            self.delayRelayList.append([relay, time.time() + delay])

    def removeDelayRelay(self, relay):
        position = 0
        for delayRelay in self.delayRelayList:
            if(delayRelay[0] == relay):
                self.delayRelayList.pop(position)
                return True
            position+=1
        return False

    def getAndRemoveFinishedRelays(self):
        currentTime = time.time()
        finishedRelays = []
        for delayRelay in self.delayRelayList:
            if(delayRelay[1] <= currentTime):
                finishedRelays.append(delayRelay[0])
        for relay in finishedRelays:
            self.removeDelayRelay(relay)
        return finishedRelays
    # Create a method to get the current
