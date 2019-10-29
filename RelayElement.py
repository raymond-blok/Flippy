class RelayElement(object):

    def __init__(self, pin):
        self.pin = pin
        # Save the pin used for this sensor.
        self.power = False

    # Create a method to turn on the RelayElement.
    def turnOn(self):
        self.power = True
        print("bob")
    # Create a method to turn off the RelayElement.
    def turnOff():
        self.power = False
