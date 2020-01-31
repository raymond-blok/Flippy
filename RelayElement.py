import wiringpi
import settings
import time

class RelayElement:
    def __init__(self,name, pin):
        self.name = name
        self.pin = pin
        #because of pull-up powering states are switched
        self.active = True
        self.timeInMillis = 0

        #Initialize pinmode output and write off
        wiringpi.pinMode(self.pin, 1)
        wiringpi.digitalWrite(self.pin, 1)

    # powering on the RelayElement.
    # returns void
    def powerOn(self):
        #check if power is off and time is later then 100 milis
        if(self.active != True and ( ( (int(round(time.time() * 1000) ) - self.timeInMillis ) > 100))):
            #Debug option
            if (settings.debugMode):
                print(self.name + " is powerd on (pull-up)")
            self.active = True
            wiringpi.digitalWrite(self.pin, self.active)

    # powerinng off the RelayElement.
    # returns void
    def powerOff(self):
        if(self.active != False):
            #Debug option
            if (settings.debugMode):
                print(self.name + " is powerd off (pull-up)")
            self.active = False
            wiringpi.digitalWrite(self.pin, self.active)
            #save start time
            self.timeInMillis = int(round(time.time() * 1000))
