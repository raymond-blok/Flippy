from GameMode import *
from GameRule import *
from HardWare import *

#Sensors
leftBumperSensor =      215
rightBumperSensor =     214
leftMushroomSensor =    213
rightMushroomSensor =   212
aboveMushroomSenor =    211
tiltSensor =            210
swingSensor =           209

middleBumpers =         315
pointSensorSerie500 =   314
upLeftRollover =        313
leftGate =              312
pointSensorSerie1000 =  311
rightUpBumper =         310
leftFlipperButton =     309
rightFlipperButton =    308

ZSensor =           415
OSensor =           414
NSensor =           413
ESensor =           412
gutterSensor =      411
holeAbove =         410
vibrationSensor =   409
startButton =       408


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
        gameRules.append(GameRule(leftFlipperButton,    leftFlipper,    0,      None))
        gameRules.append(GameRule(rightFlipperButton,   rightFlipper,   0,      None))

        gameRules.append(GameRule(ZSensor,          ZRelay,         0,      None))
        gameRules.append(GameRule(OSensor,          ORelay,         0,      None))
        gameRules.append(GameRule(NSensor,          NRelay,         0,      None))
        gameRules.append(GameRule(ESensor,          ERelay,         0,      None))
        gameRules.append(GameRule(gutterSensor,     gutterRelay,    0,      "ENDGAME"))
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
