from GameMode import *
from GameRule import *
from Hardware import *
import settings

class Game:
    def __init__(self):
        settings.init()
        gameRules = []

        gameRules.append(GameRule(settings.leftBumperSensor, settings.LeftBumperRelay,    0, None))
        gameRules.append(GameRule(settings.rightBumperSensor, settings.rightBumperRelay,   0, None))
        gameRules.append(GameRule(settings.leftMushroomSensor, settings.leftMushroomRelay,  0, None))
        gameRules.append(GameRule(settings.rightMushroomSensor, settings.rightMushroomRelay, 0, None))
        gameRules.append(GameRule(settings.aboveMushroomSenor, settings.aboveMushroomRelay, 0, None))
        gameRules.append(GameRule(settings.tiltSensor, None, 0, "ENDGAME"))
        gameRules.append(GameRule(settings.swingSensor, None, 0, "ENDGAME"))

        gameRules.append(GameRule(settings.middleBumpers, None, 0,None))
        gameRules.append(GameRule(settings.pointSensorSerie500,None, 0, None))
        gameRules.append(GameRule(settings.upLeftRollover, None, 0, None))
        gameRules.append(GameRule(settings.leftGate, None, 0, None))
        gameRules.append(GameRule(settings.pointSensorSerie1000, None, 0, None))
        gameRules.append(GameRule(settings.rightUpBumper, None, 0, None))
        gameRules.append(GameRule(settings.leftFlipperButton, settings.leftFlipper, 0, None))
        gameRules.append(GameRule(settings.rightFlipperButton, settings.rightFlipper, 0, None))

        gameRules.append(GameRule(settings.ZSensor, settings.ZRelay, 0, "zoneElement", 0, False))
        gameRules.append(GameRule(settings.OSensor, settings.ORelay, 0, "zoneElement", 0, False))
        gameRules.append(GameRule(settings.NSensor, settings.NRelay, 0, "zoneElement", 0, False))
        gameRules.append(GameRule(settings.ESensor, settings.ERelay, 0, "zoneElement", 0, False))
        gameRules.append(GameRule(settings.gutterSensor, settings.gutterRelay, 0, None))
        gameRules.append(GameRule(settings.holeAbove, settings.Hole, 0, None))
        gameRules.append(GameRule(settings.vibrationSensor, None, 0, "ENDGAME"))
        gameRules.append(GameRule(settings.startButton, None, 0, "ENDGAME"))
        self.gameMode = GameMode(gameRules)
        self.Hardware = Hardware()

        while(True):
            triggeredRelayElements = []
            activeSensorElements = self.Hardware.checkSensorElements()
            triggeredRelayElements = self.gameMode.checkRules(activeSensorElements)
            self.Hardware.activateRelayElements(triggeredRelayElements)

Game()
