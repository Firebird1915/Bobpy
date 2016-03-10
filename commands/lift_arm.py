from wpilib.command import Command

class MoveArm(Command):
    """Get the axis of the of the stick and move based
        of some conditions
    """
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.lift)
        self.setTimeout(1.0)
    
    def initialize(self):
        '''Called just before this Command runs the first time'''

    def execute(self):
        self.robot.lift.moveref(self.robot.oi.getLiftstick())

    def isFinished(self):
        return False #runs untill interrupted

    def end(self):
        "Called once after isFinshed returns True"
        self.robot.lift.stopmovement()

    def interrupted(self):
        self.end()