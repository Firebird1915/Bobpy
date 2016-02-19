from wpilib.command import Command
from subsystems.drivetrain import DriveTrain

class SpeedToggle(Command):
	def __init__(self, drivetrain):
		super().__init__()

		self.setInterruptible(False)
		self.drivetrain = drivetrain
		self.requires(drivetrain)
		self.setTimeout(1.0)

	def initialize(self):
		''' called before the command runs for the first time '''

	def execute(self):
		'''Called repeatedly when the command is scheduled to rub'''
		if self.drivetrain.is_shifted():
			self.drivetrain.shiftFast()
		else:
			self.drivetrain.shiftReturn()

	def isFinished(self):
		return False