from GameMode import *
from GameRule import *
from Hardware import *
from GameModeSelect import *

import settings

class Game:
    def __init__(self):
        settings.init()

        self.gameMode = None
        self.gameModeSelect = GameModeSelect()
        self.Hardware = Hardware()
        self.running  = False
        self.startButtonPressed = False
        self.leftFlipperButtonPressed = False
        self.rightFlipperButtonPressed = False
        while(True):
            triggeredRelayElements = []
            if(self.running):
                activeSensorElements = self.Hardware.checkSensorElements()
                triggeredRelayElements = self.gameMode.checkRules(activeSensorElements)
                self.Hardware.activateRelayElements(triggeredRelayElements)
                # W.I.P
                if(self.gameMode.gameStatus == False):
                    self.running = False
                    self.gameModeSelect = GameModeSelect()
            else:
                triggeredRelayElements = self.Hardware.checkSensorElements()
                if settings.startButton in triggeredRelayElements: # startbutton W.I.P
                    if(self.startButtonPressed == False):
                        self.startButtonPressed = True
                        if(self.gameModeSelect.nextStep()):
                            # Still need to make sure that the button is activated once per press.
                            selectedGame = self.gameModeSelect.getSelectedGameMode()
                            self.gameMode = GameMode(settings.generalGameRules, selectedGame[0], selectedGame[1])
                            self.running = True
                else:
                    self.startButtonPressed = False

                if settings.leftFlipperButton in triggeredRelayElements:

                    if(self.leftFlipperButtonPressed == False):
                        self.gameModeSelect.decrementField()
                        self.leftFlipperButtonPressed = True
                else:
                    self.leftFlipperButtonPressed = False

                if settings.rightFlipperButton in triggeredRelayElements:

                    if(self.rightFlipperButtonPressed == False):
                        self.gameModeSelect.incrementField()
                        self.rightFlipperButtonPressed = True
                    else:
                        self.rightFlipperButtonPressed = False
Game()
