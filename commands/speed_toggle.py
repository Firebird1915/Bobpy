from wpilib.command import Command
from subsystems.pneumatics_comp import Pneumatics

class SpeedToggle(Command):
    def __init__(self, pneumatics_comp):
        super().__init__()

        self.setInterruptible(False)
        self.pneumatics_comp = pneumatics_comp
        self.requires(pneumatics_comp)
        self.setTimeout(1.0)

    def initialize(self):
        ''' called before the command runs for the first time '''

    def execute(self):
        '''Called repeatedly when the command is scheduled to run'''
        
        #toggle speed modes based off of right trigger
        if not self.pneumatics_comp.shifter:
            self.pneumatics_comp.shiftFast()
            return self.setTimeout(0)
        else:
            self.pneumatics_comp.shiftReturn()
            return self.setTimeout(0)

    def isFinished(self):
        return self.isTimedOut()