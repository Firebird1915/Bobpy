import wpilib
from wpilib import SmartDashboard
from wpilib.buttons import JoystickButton

#import subsystems
from subsystems.drivetrain import DriveTrain
from subsystems.lift import LiftMech
from subsystems.pneumatics_comp import Pneumatics

#import commands
from commands.speed_toggle import SpeedToggle
from commands.pull_intake import PullIntake
from commands.lift_arm import MoveArm

class OI:

	def __init__(self, robot):
		
		#Xbox controller
		self.joy = wpilib.Joystick(0)

		#Actual Joystick
		self.joy_lift = wpilib.Joystick(1)



		#Buttons for Xbox controller
		self.r_trig = JoystickButton(self.joy, 6) #I think 

		#buttons for actual joystick
		self.btn3 = JoystickButton(self.joy_lift, 3)
		#self.btn4 = JoystickButton(self.joy_lift, 4)

		#bind buttons on Xbox controller to commands
		self.r_trig.toggleWhenPressed(SpeedToggle(robot.pneumatics_comp))


		#bind buttons on Joystick to commands
		self.btn3.whileHeld(PullIntake(robot.intake))
		#self.btn3.whenPressed(PullIntake(Intake))

	def getJoystick(self):
		return self.joy

	def getLiftstick(self):
		return self.joy_lift