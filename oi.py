import wpilib
from wpilib import SmartDashboard
from wpilib.buttons import JoystickButton
from subsystems.drivetrain import DriveTrain
from commands.speed_toggle import SpeedToggle
class OI:

	def __init__(self, robot):
		self.joy = wpilib.Joystick(0)



		#Buttons for controller
		self.r_trig = JoystickButton(self.joy, 8) #I think 

		#bind buttons to commands
		self.r_trig.toggleWhenPressed(SpeedToggle(DriveTrain))
	def getJoystick(self):
		return self.joy

