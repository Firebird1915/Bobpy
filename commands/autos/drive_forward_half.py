from wpilib.command import Command

class driveforward_half(Command):
    """
        Robot will attempt to drive for a little
            -  Yes I know its vague

    """
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.drivetrain)

    def initialize(self):
        "call before we start"
        self.robot.auto_loop_counter = 0

    def execute(self):
        self.robot.drivetrain.drive.setSafetyEnabled(False)
        self.robot.drivetrain.drive2.setSafetyEnabled(False)
        if self.robot.auto_loop_counter < 320:
            self.robot.drivetrain.drive.tankDrive(-0.6, -0.6) #drive forward
            self.robot.drivetrain.drive2.tankDrive(-0.6, -0.6)
            self.robot.auto_loop_counter += 1
        else:
            self.robot.drivetrain.drive.tankDrive(0,0)
            self.robot.drivetrain.drive2.tankDrive(0,0)
            self.robot.drivetrain.drive.setSafetyEnabled(True)
            self.robot.drivetrain.drive2.setSafetyEnabled(True)

    def isFinished(self):
        self.robot.auto_loop_counter == 320

    def end(self):
        self.robot.drivetrain.drive.tankDrive(0,0)
        self.robot.drivetrain.drive2.tankDrive(0,0)

    def interrupted(self):
        self.end()
