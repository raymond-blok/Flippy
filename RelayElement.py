import wiringpi
import settings

class RelayElement:
    def __init__(self,name, pin):
        self.name = name
        self.pin = pin
        self.active = False

        #Initialize pinmode output and write off
        wiringpi.pinMode(self.pin, 1)
        wiringpi.digitalWrite(self.pin, 1)
        
        # Save the pin used for this sensor.
        self.power = 1

    #Turn on the RelayElement.
    def turnOn(self):
        if(self.power != 0):
            #Debug option
            if (settings.debugMode):
                print(self.name + " is turned on")
            self.power = 0
            wiringpi.digitalWrite(self.pin, self.power)

    # Turn off the RelayElement.
    def turnOff(self):
        if(self.power != 1):
            #Debug option
            if (settings.debugMode):
                print(self.name + " is turned off")
            self.power = 1
            wiringpi.digitalWrite(self.pin, self.power)