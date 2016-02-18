import wpilib
from wpilib import SmartDashboard
from wpilib.buttons import JoystickButton

class OI:

	def __init__(self, robot):
		self.joy = wpilib.Joystick(0)



		#Buttons for controller
		self.r_trig = JoystickButton(self.joy, 0) #working this out 

		#bind buttons to commands
		#self.r_trig.toggleWhenPressed()
	def getJoystick(self):
		return self.joy