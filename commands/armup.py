from wpilib.command import Command
from subsystems.lift import LiftMech

class armUp(Command):
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
        self.lift.Moveup()

    def isFinished(self):
        self.isTimedOut()


        