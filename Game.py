from GameMode import *
from GameRule import *
from HardWare import *

#Sensors
leftBumperSensor =      208
rightBumperSensor =     209
leftMushroomSensor =    210
rightMushroomSensor =   211
aboveMushroomSenor =    212
tiltSensor =            213
swingSensor =           214

middleBumpers =         308
pointSensorSerie500 =   309
upLeftRollover =        310
leftGate =              311
pointSensorSerie1000 =  312
rightUpBumper =         313
leftFlipperButton =     314
rightFlipperButton =    315

ZSensor =           408
OSensor =           409
NSensor =           410
ESensor =           411
gutterSensor =      412
holeAbove =         413
vibrationSensor =   414
startButton =       415


#Relay's
gutterRelay =       307
rightFlipper =      306
rightBumperRelay =  305
ZRelay =            304
ORelay =            303
NRelay =            302
ERelay =            301

Hole =               407
leftFlipper =        406
LeftBumperRelay =    405
leftMushroomRelay =  404
rightMushroomRelay = 403
aboveMushroomRelay = 402


class Game(object):
    def __init__(self):
        gameRules = []

        gameRules.append(GameRule(leftBumperSensor,     LeftBumperRelay,    0, None))
        gameRules.append(GameRule(rightBumperSensor,    rightBumperRelay,   0, None))
        gameRules.append(GameRule(leftMushroomSensor,   leftMushroomRelay,  0, None))
        gameRules.append(GameRule(rightMushroomSensor,  rightMushroomRelay, 0, None))
        gameRules.append(GameRule(aboveMushroomSenor,   aboveMushroomRelay, 0, None))
        gameRules.append(GameRule(tiltSensor,           None,               0, "ENDGAME"))
        gameRules.append(GameRule(swingSensor,          None,               0, "ENDGAME"))

        gameRules.append(GameRule(middleBumpers,        None,           0,      None))
        gameRules.append(GameRule(pointSensorSerie500,  None,           0,      None))
        gameRules.append(GameRule(upLeftRollover,       None,           0,      None))
        gameRules.append(GameRule(leftGate,             None,           0,      None))
        gameRules.append(GameRule(pointSensorSerie1000, None,           0,      None))
        gameRules.append(GameRule(rightUpBumper,        None,           0,      None))
        gameRules.append(GameRule(leftFlipperButton,    gutterRelay,    0,      None))
        gameRules.append(GameRule(rightFlipperButton,   rightFlipper,   0,      None))

        gameRules.append(GameRule(ZSensor,          ZRelay,         0,      None))
        gameRules.append(GameRule(OSensor,          ORelay,         0,      None))
        gameRules.append(GameRule(NSensor,          NRelay,         0,      None))
        gameRules.append(GameRule(ESensor,          ERelay,         0,      None))
        gameRules.append(GameRule(gutterSensor,     gutterRelay,    0,      None))
        gameRules.append(GameRule(holeAbove,        Hole,           0,      None))
        gameRules.append(GameRule(vibrationSensor,  None,           0,      "ENDGAME"))
        gameRules.append(GameRule(startButton,      None,           0,      "ENDGAME"))
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
