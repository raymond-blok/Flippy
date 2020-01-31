import wiringpi
import settings

class SensorElement:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.active = False

        # Save the pin used for this sensor.
        wiringpi.pinMode(self.pin, 0)
        wiringpi.pullUpDnControl(self.pin, 2)

    # this is a method to check if a sensor is triggered.
    # returns (boolean) True if active.
    def checkSensor(self):
        sensorValue = 1 - wiringpi.digitalRead(self.pin) # invert because of pullup.
        if(sensorValue == 1):
            if(self.active != True):
                self.active = True
                #Debug option
                if (settings.debugMode):
                    print(self.name + " is triggered")
            return True
        else:
            self.active = False
            return False
