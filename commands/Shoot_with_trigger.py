from wpilib.command import Command

class ShootWithTrigger(Command):
	'''
		Have the robot wind up the shoot mech with the trigger and shoot at a certain position.
	'''
	def __init__(self, robot):
		super().__init__()

		self.robot = robot
		self.requires(self.robot.Shooter)

	def initialize(self):
        '''Called just before this Command runs the first time'''

    def execute(self):
        '''Called repeatedly when this Command is scheduled to run'''
    	pass

    def isFinished(self):
        '''Make this return true when this Command no longer needs to run execute()'''
        return False

    def end(self):
        '''Called once after isFinished returns true'''
    	pass

    def interrupted(self):
        '''Called when another command which requires one or more of the same
           subsystems is scheduled to run'''
        self.end()