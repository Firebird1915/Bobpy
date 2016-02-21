from wpilib.command import Command
from subsystems.pneumatics_comp import Pneumatics

class SpeedToggle(Command):
    def __init__(self, pneumatics):
        super().__init__()

        self.setInterruptible(False)
        self.pneumatics = pneumatics
        self.requires(pneumatics)
        self.setTimeout(1.0)

    def initialize(self):
        ''' called before the command runs for the first time '''

    def execute(self):
        '''Called repeatedly when the command is scheduled to run'''
        
        #toggle speed modes based off of right trigger
        if self.pneumatics.is_shifted():
            self.pneumatics.shiftFast()
        else:
            self.pneumatics.shiftReturn()

    def isFinished(self):
        return self.isTimedOut()