import wpilib
from wpilib.command import Subsystem

class LiftMech(Subsystem):
	""" The arm works with only one motor gearbox with
		a 10:1 gear ratio.
	"""
	def __init__(self, robot):
		super().__init__()
		self.robot = robot

		self.armMotor = wpilib.CANTalon(12)

		self.sd = wpilib.SmartDashboard

	def moveUp(self):
		self.armMotor.set(-0.5)

	def moveDown(self):
		self.armMotor.set(0.5)

	def log(self):
		self.sd.putDouble("Arm Distance", self.armMotor.getEncPosition())
