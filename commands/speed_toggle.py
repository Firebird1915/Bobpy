from wpilib.command import Command


class SpeedToggle(Command):
    def __init__(self, robot):
        super().__init__()

        self.setInterruptible(False)
        self.robot = robot
        self.requires(self.robot.pneumatics)
        self.setTimeout(1.0)

    def initialize(self):
        ''' called before the command runs for the first time '''

    def execute(self):
        '''Called repeatedly when the command is scheduled to run'''
        
        #toggle speed modes based off of right trigger
        if self.robot.pneumatics.is_shifted():
            self.robot.pneumatics.shiftFast()
        else:
            self.robot.pneumatics.shiftReturn()

    def isFinished(self):
        return False