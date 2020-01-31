class GameModeSelect:

    def __init__(self):
        self.GameModes = []
        self.GameModes.append({"name": "normal"})
        self.selectedMode = [1,1]
        self.currentField = 0
        self.max = [4, 3]
        self.min = [1, 1]
            # Initialize a list of GameModes

            # list of current hardware components.
    # function to add an amount to field.
    def incrementField(self):
        if(self.max[self.currentField] > self.selectedMode[self.currentField]):
            print("increment")
            self.selectedMode[self.currentField] = self.selectedMode[self.currentField] + 1
        # function to decrease amount to field.
    def decrementField(self):
        if(self.min[self.currentField] < self.selectedMode[self.currentField]):
            print("decrement")
            self.selectedMode[self.currentField] = self.selectedMode[self.currentField] - 1

    # function to go to the next step.
    def nextStep(self):
        if(self.currentField < 1):
            self.currentField = self.currentField + 1
            return False
        return True

    def getSelectedGameMode(self):
        print("mode")
        print(self.selectedMode)
        return self.selectedMode
