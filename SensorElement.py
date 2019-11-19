import wiringpi
import time
import settings

class SensorElement:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.time = 0
        self.active = False
        
        # Save the pin used for this sensor.
        wiringpi.pinMode(self.pin, 0)
        wiringpi.pullUpDnControl(self.pin, 2)

    # Create a method to check if the sensor is active.
    def checkSensor(self):
        sensorValue = 1 - wiringpi.digitalRead(self.pin) # invert because of pullup.
        if(sensorValue == 1):
            if(self.active == False):
                self.time = time.monotonic()
                self.active = True
            if(self.active and (time.monotonic() - self.time) > 0.0001):
                # DEBUG
                if (settings.debugMode):
                    print(self.name + " is active in SensorElement")
                return True
            else:
                return False
        else:
            self.active = False
            return False
