import wpilib
from wpilib.command import Subsystem


class Shooter(Subsystem):
	"""Subsystem for shooter mechanism
	"""
	def __init__(self, robot):
		super().__init__()
		self.robot = robot

		self.shoot_motor = wpilib.CANTalon(7)

	
		