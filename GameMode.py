from GameRule import *
import settings
import time

class GameMode:
    def __init__(self, gameRules, players, attempts):
        self.players = players
        # Save a list of GameRules.
        self.gameRules = gameRules
        # Keep the total score
        self.score = [0] * self.players
        self.attempts = [attempts] * self.players

        self.currentPlayer = 0
        # list to keep the zone relayList
        self.zoneRelayList = []
        self.delayRelayList = []



        self.gameStatus = True
        self.addDelayRelay(settings.gutterRelay, 0)
        self.gameStart = False
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
                                print("test")
                                self.addDelayRelay(relayElement, gameRule.delay)

            if(check == False):
                gameRule.deactivate()
                self.deactivateSpecialCase(gameRule)
        triggeredRelayElements += self.getAndRemoveFinishedRelays()
        self.gameStart = True
        return triggeredRelayElements

    # Create a method to check and add the score.
    def checkAndAddScore(self, gameRule):
        self.score[self.currentPlayer] += gameRule.getPoints()

    # Create a method to check special circumstances.
    def checkSpecialCase(self, gameRule):
        case = gameRule.getSpecialCase()
        if(case == None):
            return
        if(case == "ENDGAME"):
            if(self.gameStart):
                self.endGame()
            return
        if(case == "zoneElement"):
            self.zoneRelayList.append(gameRule.relayElement)
            print(self.zoneRelayList)
            if(len(self.zoneRelayList) >= 4):
                for zoneRelay in self.zoneRelayList:
                    self.addDelayRelay(zoneRelay, 5)

    def deactivateSpecialCase(self, gameRule):
        case = gameRule.getSpecialCase()
        if(case == None):
            return
        if(case == "zoneElement"):
            if (gameRule.relayElement in self.zoneRelayList):
                self.zoneRelayList.remove(gameRule.relayElement)
    # Create a method to end the game.
    def endGame(self):
        if all(x <= 0 for x in self.attempts):
            self.gameStatus = False
            self.score = [0] * self.players
            print("ahahh")
            return
        print(self.attempts[self.currentPlayer])
        self.attempts[self.currentPlayer] = self.attempts[self.currentPlayer] - 1
        self.addDelayRelay(settings.gutterRelay, 1)
        if(self.attempts[self.currentPlayer] <= 0 and self.currentPlayer > self.players):
            self.currentPlayer = self.currentPlayer + 1



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
