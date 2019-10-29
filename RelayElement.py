import wiringpi

class RelayElement(object):

    def __init__(self, pin):
        self.pin = pin
        wiringpi.pinMode(self.pin, 1)
        wiringpi.digitalWrite(self.pin, 0)
        # Save the pin used for this sensor.
        self.power = False

    # Create a method to turn on the RelayElement.
    def turnOn(self):
        self.power = True
        wiringpi.digitalWrite(self.pin, self.power)

    # Create a method to turn off the RelayElement.
    def turnOff():
        self.power = False
        wiringpi.digitalWrite(self.pin, self.power)
