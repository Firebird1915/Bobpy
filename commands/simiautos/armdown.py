from wpilib.command import Command
from subsystems.lift import LiftMech

class armDown(Command):
    """
        Command for rasing the arm some position
     """
    def __init__(self, lift):
        super().__init__()
        self.lift = lift
        self.requires(lift)

    def initalize(self):
        '''Called just before this Command runs the first time'''

    def execute(self):
        self.lift.moveDown()

    def isFinished(self):
        self.isTimedOut()
