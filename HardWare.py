from SensorElement import *
from RelayElement import *
import wiringpi

class HardWare(object):

    def __init__(self):
        wiringpi.wiringPiSetup()
        wiringpi.mcp23017Setup(65, 0x20)
        # Hold a list of Sensors
        self.sensorElements = []
        self.sensorElements.append(SensorElement(65))
        # Hold a list of RelayElements
        self.relayElements = []
        self.relayElements.append(RelayElement(66))
        # Initialize wiringpi


    # Create a method to Scan a list of Sensors.
    def checkSensorElements(self):
        activeSensorElements = []
        for sensorElement in self.sensorElements:
            if(sensorElement.checkSensor()):
                activeSensorElements.append(sensorElement.pin)
        return activeSensorElements

    # Create a method to activate a RelayElement
    def activateRelayElements(self, triggeredRelayElements):
        for relayElement in self.relayElements:
            for triggeredRelayElement in triggeredRelayElements:
                if(relayElement.pin == triggeredRelayElement):
                    relayElement.turnOn()
                    break
            relayElement.turnOff()
