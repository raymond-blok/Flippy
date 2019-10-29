class GameRule(object):
    def __init__(self, sensor, relayElement, score, specialCase = None):
        # save a sensor to a field.
        self.sensor = sensor
        # save a (potential) RelayElement.
        self.relayElement = relayElement
        # save the amount of point to a field.
        self.score = score
        # Special case
        self.specialCase = specialCase

    # Create a method to return the Sensor.
    def getSensor(self):
        return self.sensor
    # Create a method to return the (potential) RelayElement.
    def getRelayElement(self):
        return self.relayElement
    # Create a method to return the points.
    def getPoints(self):
        return self.score
    # Create a method to return special cases.
    def getSpecialCase(self):
        return self.specialCase
