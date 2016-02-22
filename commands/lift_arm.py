from wpilib.command import Command
from subsystems.lift import LiftMech

class MoveArm(Command):
	"""Get the axis of the of the stick and move based
		of some conditions
	"""
	def __init__(self, LiftMech):
		super().__init__()
		self.LiftMech = LiftMech
		self.requires(LiftMech)
	
	def initialize(self):
        '''Called just before this Command runs the first time'''

    def execute(self):
    	pass