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
        # this is so that the ball returns at the start of the game.
        self.addDelayRelay(settings.gutterRelay, 0)
        self.resetZone();
        self.addDelayRelay(settings.leftFlipper, 0)
        self.gameStart = False
    # this method checks the list with GameRules.
    #param int[] this is a list of active Sensors
    #returns int[] this is a list of relays that need to be activated.
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
                            self.checkAndAddScore(gameRule.getPoints())
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
                self.deactivateSpecialCase(gameRule)
        triggeredRelayElements += self.getAndRemoveFinishedRelays()
        self.gameStart = True
        return triggeredRelayElements

    # this method adds the score if it can.
    # param int this is the amount of points to add.
    # return void
    def checkAndAddScore(self, points):
        if(self.gameStatus == True):
            self.score[self.currentPlayer] += points

    # this is a method for when a rule requires extra funcionality behond the standard.
    # param GameRule this is the gamerule to checks
    # return void
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
                self.checkAndAddScore(10000)
                for zoneRelay in self.zoneRelayList:
                    self.addDelayRelay(zoneRelay, 5)

    def deactivateSpecialCase(self, gameRule):
        case = gameRule.getSpecialCase()
        if(case == None):
            return
        if(case == "zoneElement"):
            if (gameRule.relayElement in self.zoneRelayList):
                self.zoneRelayList.remove(gameRule.relayElement)

    # this method ends the current turn of an player
    # return void
    def endGame(self):
        allDone = True
        for attempt in self.attempts:
            if(attempt > 0):
                allDone = False
        if(allDone == True):
            self.gameStatus = False
            return
        print(self.attempts[self.currentPlayer])
        self.attempts[self.currentPlayer] = self.attempts[self.currentPlayer] - 1
        self.resetZone();
        if(self.attempts[self.currentPlayer] <= 0 and self.currentPlayer < self.players-1):
            self.currentPlayer = self.currentPlayer + 1


    #this method checks if an relay is already active to prevent doubles.
    # param (int): the relay to check
    # returns (boolean): returns false if already in the list.
    def checkDelayRelay(self, relay):
        for delayRelay in self.delayRelayList:
            if(delayRelay[0] == relay):
                return False
        return True

    # This method adds the relay to the delay list if it does not exist yet.
    # param (int) the relay to add.
    # param (int) the amount to delay the relay activation.
    # returns void
    def addDelayRelay(self, relay, delay):
        if(self.checkDelayRelay(relay)):
            self.delayRelayList.append([relay, time.time() + delay])

    #removes a relay form the delay list
    #param (int) this is the relay to remove from the list.
    #returns (boolean): true if the removal was successful.
    def removeDelayRelay(self, relay):
        position = 0
        for delayRelay in self.delayRelayList:
            if(delayRelay[0] == relay):
                self.delayRelayList.pop(position)
                return True
            position+=1
        return False

    #this method removes and returns the relays that are ready to be executed.
    #returns (int[]) the relays that are ready for activation.
    def getAndRemoveFinishedRelays(self):
        currentTime = time.time()
        finishedRelays = []
        for delayRelay in self.delayRelayList:
            if(delayRelay[1] <= currentTime):
                finishedRelays.append(delayRelay[0])
        for relay in finishedRelays:
            self.removeDelayRelay(relay)
        return finishedRelays
    # this method resets the zone if nessesery.
    # returns void
    def resetZone(self):
        self.addDelayRelay(settings.ZRelay, 0)
        self.addDelayRelay(settings.ORelay, 0)
        self.addDelayRelay(settings.NRelay, 0)
        self.addDelayRelay(settings.ERelay, 0)
