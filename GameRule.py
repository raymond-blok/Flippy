class GameRule:
    def __init__(self, sensorElement, relayElement, score, specialCase = None):
        # save a sensor to a field.
        self.sensorElement = sensorElement

        # save a (potential) RelayElement.
        self.relayElement = relayElement

        # save the amount of point to a field.
        self.score = score

        # Special case
        self.specialCase = specialCase
        self.active = False
        self.triggered = False

    # Create a method to return the Sensor.
    def getSensor(self):
        return self.sensorElement

    # Create a method to return the RelayElement.
    def getRelayElement(self):
        return self.relayElement

    # Create a method to return the points.
    def getPoints(self):
        return self.score

    # Create a method to return special cases.
    def getSpecialCase(self):
        return self.specialCase

    def activate(self):
        if(self.active):
            return True
        else:
            self.active = True
            return True

    def deactivate(self):
        self.triggered = False
        self.active = False
