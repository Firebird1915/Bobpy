import wpilib
from wpilib.command import Command
from subsystems.intake import Intake

class PushOutBall(Command):
    """wind up motors on cue"""
    def __init__(self, intake):
        super().__init__()
        self.intake = intake
        self.requires(intake)

    def initialize(self):
        '''called before the command runs for the first time'''

    def execute(self):
        ''' Called repeatedly when the command is scheduled to run '''
        loseball()
        return self.setTimeout(0)

    def isFinished(self):
        return self.isTimedOut()