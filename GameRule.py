import time
class GameRule:
    def __init__(self, sensor, relayElement, score, specialCase = None, delay = 0):
        # save a sensor to a field.
        self.sensor = sensor

        # save a (potential) RelayElement.
        self.relayElement = relayElement

        # save the amount of point to a field.
        self.score = score

        # Special case
        self.specialCase = specialCase
        self.active = False
        self.delay = delay
        self.triggered = False
        self.time = 0;

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

    def activate(self):
        if(self.delay == 0):
            self.active = True
            return True
        if(self.active):
            if(self.active and (time.monotonic() - self.time) > self.delay):
                return True
            else:
                return False
        else:
            self.active = True
            self.time = time.monotonic()
            return False


    def deactivate(self):
        self.triggered = False
        self.active = False
