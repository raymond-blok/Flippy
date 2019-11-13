from SensorElement import *
from RelayElement import *
import wiringpi as wiringpi

class HardWare(object):
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
        # Hold a list of Sensors
        self.sensorElements = []
        for i in range(7):
            self.sensorElements.append(SensorElement(mcpTwoPin + 9 + i))
        for i in range(8):
            self.sensorElements.append(SensorElement(mcpThreePin + 8 + i))
        for i in range(8):
            self.sensorElements.append(SensorElement(mcpFourPin + 8 + i))
        # Hold a list of RelayElements
        self.relayElements = []
        self.relayElements.append(RelayElement(66))
        for i in range(7):
            self.relayElements.append(RelayElement(mcpThreePin + 1 + i))
        for i in range(6):
            self.relayElements.append(RelayElement(mcpFourPin + 2 + i))


    # Create a method to scan a list of Sensors.
    def checkSensorElements(self):
        activeSensorElements = []
        for sensorElement in self.sensorElements:
            if(sensorElement.checkSensor()):
                activeSensorElements.append(sensorElement.pin)
        return activeSensorElements

    # Create a method to activate a RelayElement
    def activateRelayElements(self, triggeredRelayElements):
        print("elements to activate")
        print(triggeredRelayElement)
        for relayElement in self.relayElements:
            check = False
            for triggeredRelayElement in triggeredRelayElements:
                if(relayElement.pin == triggeredRelayElement):
                    relayElement.turnOn()
                    check = True
                    break
            if(check == False):
                relayElement.turnOff()
