import GameRule
debugMode =             True

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

ZSensor =               408
OSensor =               409
NSensor =               410
ESensor =               411
gutterSensor =          412
holeAbove =             413
vibrationSensor =       414
startButton =           415

#Relay's
gutterRelay =           307
rightFlipper =          306
rightBumperRelay =      305
ZRelay =                304
ORelay =                303
NRelay =                302
ERelay =                301

Hole =                  407
leftFlipper =           401
LeftBumperRelay =       405
leftMushroomRelay =     404
rightMushroomRelay =    403
aboveMushroomRelay =    402

def init():
    global sensorList
    global relayList
    global generalGameRules

    #sensorList with name and pin
    sensorList = []
    sensorList.append(["leftBumperSensor", leftBumperSensor])
    sensorList.append(["rightBumperSensor", rightBumperSensor])
    sensorList.append(["leftMushroomSensor", leftMushroomSensor])
    sensorList.append(["rightMushroomSensor", rightMushroomSensor])
    sensorList.append(["aboveMushroomSenor", aboveMushroomSenor])
    sensorList.append(["tiltSensor", tiltSensor])
    sensorList.append(["swingSensor", swingSensor])
    sensorList.append(["middleBumpers", middleBumpers])
    sensorList.append(["pointSensorSerie500", pointSensorSerie500])
    sensorList.append(["upLeftRollover", upLeftRollover])
    sensorList.append(["leftGate", leftGate])
    sensorList.append(["pointSensorSerie1000", pointSensorSerie1000])
    sensorList.append(["rightUpBumper", rightUpBumper])
    sensorList.append(["leftFlipperButton", leftFlipperButton])
    sensorList.append(["rightFlipperButton", rightFlipperButton])
    sensorList.append(["ZSensor", ZSensor])
    sensorList.append(["OSensor", OSensor])
    sensorList.append(["NSensor", NSensor])
    sensorList.append(["ESensor", ESensor])
    sensorList.append(["gutterSensor", gutterSensor])
    sensorList.append(["holeAbove", holeAbove])
    sensorList.append(["vibrationSensor", vibrationSensor])
    sensorList.append(["startButton", startButton])

    #relayList with name and pin
    relayList = []
    relayList.append(["gutterRelay", gutterRelay])
    relayList.append(["rightFlipper", rightFlipper])
    relayList.append(["leftFlipper", leftFlipper])
    relayList.append(["rightBumperRelay", rightBumperRelay])
    relayList.append(["LeftBumperRelay", LeftBumperRelay])
    relayList.append(["ZRelay", ZRelay])
    relayList.append(["ORelay", ORelay])
    relayList.append(["NRelay", NRelay])
    relayList.append(["ERelay", ERelay])
    relayList.append(["Hole", Hole])
    relayList.append(["leftMushroomRelay", leftMushroomRelay])
    relayList.append(["rightMushroomRelay", rightMushroomRelay])
    relayList.append(["aboveMushroomRelay", aboveMushroomRelay])

    generalGameRules = []

    generalGameRules.append(GameRule.GameRule(leftBumperSensor, LeftBumperRelay,    0, None))
    generalGameRules.append(GameRule.GameRule(rightBumperSensor, rightBumperRelay,   0, None))
    generalGameRules.append(GameRule.GameRule(leftMushroomSensor, leftMushroomRelay,  0, None))
    generalGameRules.append(GameRule.GameRule(rightMushroomSensor, rightMushroomRelay, 0, None))
    generalGameRules.append(GameRule.GameRule(aboveMushroomSenor, aboveMushroomRelay, 0, None))
    generalGameRules.append(GameRule.GameRule(tiltSensor, None, 0, "ENDGAME"))
    generalGameRules.append(GameRule.GameRule(swingSensor, None, 0, "ENDGAME"))

    generalGameRules.append(GameRule.GameRule(middleBumpers, None, 0,None))
    generalGameRules.append(GameRule.GameRule(pointSensorSerie500,None, 500, None))
    generalGameRules.append(GameRule.GameRule(upLeftRollover, None, 100, None))
    generalGameRules.append(GameRule.GameRule(leftGate, None, 200, None))
    generalGameRules.append(GameRule.GameRule(pointSensorSerie1000, None, 1000, None))
    generalGameRules.append(GameRule.GameRule(rightUpBumper, None, 0, None))
    generalGameRules.append(GameRule.GameRule(leftFlipperButton, leftFlipper, 0, None))
    generalGameRules.append(GameRule.GameRule(rightFlipperButton, rightFlipper, 0, None))

    generalGameRules.append(GameRule.GameRule(ZSensor, ZRelay, 0, "zoneElement", 0, False))
    generalGameRules.append(GameRule.GameRule(OSensor, ORelay, 0, "zoneElement", 0, False))
    generalGameRules.append(GameRule.GameRule(NSensor, NRelay, 0, "zoneElement", 0, False))
    generalGameRules.append(GameRule.GameRule(ESensor, ERelay, 0, "zoneElement", 0, False))
    generalGameRules.append(GameRule.GameRule(gutterSensor, gutterRelay, 0, "ENDGAME", 1))
    generalGameRules.append(GameRule.GameRule(holeAbove, Hole, 1000, None, 2))
    generalGameRules.append(GameRule.GameRule(vibrationSensor, None, 0, "ENDGAME"))
    generalGameRules.append(GameRule.GameRule(startButton, None, 0, "ENDGAME"))
