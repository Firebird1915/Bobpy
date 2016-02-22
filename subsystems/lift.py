import wpilib
from wpilib.command import Subsystem
from commands.lift_arm import MoveArm

class LiftMech(Subsystem):
	""" The arm works with only one motor gearbox with
		a 10:1 gear ratio.
	"""
	def __init__(self, robot):
		super().__init__()
		self.robot = robot

		self.armMotor = wpilib.CANTalon(12)

		self.sd = wpilib.SmartDashboard

	def initDefaultCommand(self):
		self.setDefaultCommand(MoveArm(self.robot))

	def moveUp(self):
		self.armMotor.set(-0.5)

	def moveDown(self):
		self.armMotor.set(0.5)

	def stopmovement(self):
		self.armMotor.set(0)

	def moveref(self, joy_lift):
		if joy_lift.getRawAxis(1) == 1:
			self.armMotor.set(0.5)
		elif joy_lift.getRawAxis(1) == -1:
			self.armMotor.set(-0.5)
		else:
			self.armMotor.set(0)


	def log(self):
		self.sd.putDouble("Arm Distance", self.armMotor.getEncPosition())
