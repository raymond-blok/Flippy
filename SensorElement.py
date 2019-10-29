import wiringpi2 as wiringpi

class SensorElement(object):

    def __init__(self, pin):
        self.pin = pin
        # Save the pin used for this sensor.
        wiringpi.pinMode(self.pin, 0)
        wiringpi.pullUpDnControl(self.pin, 2)

    # Create a method to check if the sensor is active.
    def checkSensor(self):
        return wiringpi.digitalRead(self.pin)
