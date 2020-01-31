class GameRule:
    def __init__(self, sensorElement, relayElement, score, specialCase = None, delay = 0, addRelay = True):
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
        self.addRelay = addRelay
        self.delay = delay

    # getter of the sensor
    # returns (int): the sensor
    def getSensor(self):
        return self.sensorElement

    # getter for the relay element.
    def getRelayElement(self):
        if(self.addRelay):
            return self.relayElement
        return None

    # getter for points.
    def getPoints(self):
        return self.score

    # getter for the specialcase
    def getSpecialCase(self):
        return self.specialCase

    # activates the GameRule
    # returns true if the rule is active
    def activate(self):
        if(self.active):
            return True
        else:
            self.active = True
            return True

    # deactivates the game rule.
    # returns void
    def deactivate(self):
        self.triggered = False
        self.active = False
