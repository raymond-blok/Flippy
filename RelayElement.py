import wiringpi as wiringpi

class RelayElement(object):
    def __init__(self, pin):
        #Initialize pinmode output and write off
        self.pin = pin
        wiringpi.pinMode(self.pin, 1)
        wiringpi.digitalWrite(self.pin, 1)
        # Save the pin used for this sensor.
        self.power = 1

    # Create a method to turn on the RelayElement.
    def turnOn(self):
        if(self.power != 0):
            print("RelayElement " + str(self.pin) + " is turned on")
            self.power = 0
            wiringpi.digitalWrite(self.pin, self.power)

    # Create a method to turn off the RelayElement.
    def turnOff(self):
        if(self.power != 1):
            self.power = 1
            wiringpi.digitalWrite(self.pin, self.power)
