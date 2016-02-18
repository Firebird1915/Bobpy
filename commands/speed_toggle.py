from wpilib.command import Command
from subsystems.drivetrain import DriveTrain

class SpeedToggle(Command):
	def __init__(self, drivetrain):
		super().__init__()

		self.setInterruptible(False)
		self.robot = robot
		self.requires(self.robot.drivetrain)
		self.setTimeout(1.0)

	def initialize(self):
		''' called before the command runs for the first time '''

	def execute(self):
		'''Called repeatedly when the command is scheduled to rub'''
		pass

	def isFinished(self):
		return False