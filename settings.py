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
leftFlipper =           406
LeftBumperRelay =       405
leftMushroomRelay =     404
rightMushroomRelay =    403
aboveMushroomRelay =    402

def init():
    global sensorList
    global relayList

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
