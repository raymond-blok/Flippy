from SensorElement import *
from RelayElement import *
import wiringpi
import settings
import time

class Hardware:
    def __init__(self):
        # Initialize wiringpi
        wiringpi.wiringPiSetup()
        mcpOnePin = 100
        mcpTwoPin = 200
        mcpThreePin = 300
        mcpFourPin = 400
        wiringpi.mcp23017Setup(mcpOnePin, 0x20)
        wiringpi.mcp23017Setup(mcpTwoPin, 0x21)
        wiringpi.mcp23017Setup(mcpThreePin, 0x22)
        wiringpi.mcp23017Setup(mcpFourPin, 0x23)

        # Hold a list of Sensors objects
        self.sensorElements = []
        for sensorElement in settings.sensorList:
            self.sensorElements.append(SensorElement(sensorElement[0], sensorElement[1]))

        # Hold a list of RelayElements objects
        self.relayElements = []
        for relayElement in settings.relayList:
            self.relayElements.append(RelayElement(relayElement[0], relayElement[1]))

    # scan a list of Sensors to see if active
    # returns(int[]) the acitve senors
    def checkSensorElements(self):
        activeSensorElements = []
        for sensorElement in self.sensorElements:
            if(sensorElement.checkSensor()):
                activeSensorElements.append(sensorElement.pin)
        return activeSensorElements

    # activate relayelements in the in the given list
    #params (int[]) relays to activate.
    # returns void
    def activateRelayElements(self, triggeredRelayElements):
        for relayElement in self.relayElements:
            isChecked = False
            for triggeredRelayElement in triggeredRelayElements:
                if(relayElement.pin == triggeredRelayElement):
                    relayElement.powerOff()
                    isChecked = True
                    break
            if(isChecked != True):
                relayElement.powerOn()
    def testRelays(self):
        for relay in self.relayElements:
            relay.powerOff()
            time.sleep(0.3)
            relay.powerOn()
