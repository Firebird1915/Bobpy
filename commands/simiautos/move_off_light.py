from wpilib.command import Command

class MoveOffLight(Command):
    """
        robot will attemp to move forward untill light sensor
        picks up something

    """
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.drivetrain)

    def initialize(self):
        "call before we start"

    def execute(self):
        self.robot.drivetrain.drive.setSafetyEnabled(False)
        self.robot.drivetrain.drive2.setSafetyEnabled(False)
        if self.robot.drivetrain.photo.get() == False:
            self.robot.drivetrain.drive.tankDrive(-0.5, -0.5) #drive forward
            self.robot.drivetrain.drive2.tankDrive(-0.5, -0.5)
        else:
            self.robot.drivetrain.drive.tankDrive(0,0)
            self.robot.drivetrain.drive2.tankDrive(0,0)
            self.robot.drivetrain.drive.setSafetyEnabled(True)
            self.robot.drivetrain.drive2.setSafetyEnabled(True)

    def isFinished(self):
        self.robot.drivetrain.photo == True

    def end(self):
        self.robot.drivetrain.drive.tankDrive(0,0)
        self.robot.drivetrain.drive2.tankDrive(0,0)

    def interrupted(self):
        self.end()
