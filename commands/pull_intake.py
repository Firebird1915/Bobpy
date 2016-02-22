from wpilib.command import Command
from subsystems.intake import Intake

class PullIntake(Command):
	"""docstring for pull_intake"""
	def __init__(self, Intake):
		super().__init__()
		self.Intake = Intake
		self.requires(Intake)

	def initialize(self):
		'''Call for the first time'''

	def execute(self):
		'''Called Repeatedly when scheduled to run'''

		self.intake.takeball()

	def isFinished(self):
		self.end()
