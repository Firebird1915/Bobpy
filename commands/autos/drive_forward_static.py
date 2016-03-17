from wpilib.command import Command

class driveforward_static(Command):
    """
        robot will attemp to jump the static obstacle in autonomous
            - It is pretty consistant with category B & D defenses

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
        if self.robot.auto_loop_counter < 240:
            self.robot.drivetrain.drive.tankDrive(-0.8, -0.8) #drive forward
            self.robot.drivetrain.drive2.tankDrive(-0.8, -0.8)
            self.robot.auto_loop_counter += 1
        else:
            self.robot.drivetrain.drive.tankDrive(0,0)
            self.robot.drivetrain.drive2.tankDrive(0,0)
            self.robot.drivetrain.drive.setSafetyEnabled(True)
            self.robot.drivetrain.drive2.setSafetyEnabled(True)

    def isFinished(self):
        self.robot.auto_loop_counter == 240

    def end(self):
        self.robot.drivetrain.drive.tankDrive(0,0)
        self.robot.drivetrain.drive2.tankDrive(0,0)

    def interrupted(self):
        self.end()