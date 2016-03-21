import wpilib
from wpilib import SmartDashboard
from wpilib.buttons import JoystickButton

#import subsystems
from subsystems.drivetrain import DriveTrain
from subsystems.lift import LiftMech
from subsystems.pneumatics_comp import Pneumatics

#import commands
from commands.speed_toggle import SpeedToggle
from commands.lift_arm import MoveArm
from commands.simiautos.armup import armUp
from commands.shootpiston import shoot_piston
from commands.take_in_ball import TakeInBall
from commands.push_out_ball import PushOutBall
class OI:

	def __init__(self, robot):

		#Xbox controller
		self.joy = wpilib.Joystick(0)

		#Actual Joystick
		self.joy_lift = wpilib.Joystick(1)



		#Buttons for Xbox controller
		self.r_trig = JoystickButton(self.joy, 6) #I think

		#buttons for actual joystick

		self.btn1 = JoystickButton(self.joy_lift, 1)
		self.btn2 = JoystickButton(self.joy_lift, 2) #shooter button
		self.btn3 = JoystickButton(self.joy_lift, 3)
		self.btn4 = JoystickButton(self.joy_lift, 4)
		self.btn5 = JoystickButton(self.joy_lift, 5)
		self.btn7 = JoystickButton(self.joy_lift, 7)

		#bind buttons on Xbox controller to commands
		self.r_trig.toggleWhenPressed(SpeedToggle(robot.pneumatics_comp))


		#bind buttons on Joystick to commands
		self.btn7.whenPressed(armUp(robot.lift))


		self.btn1.whenPressed(shoot_piston(robot.pneumatics_comp))

		#intake related commands
		self.btn3.whileHeld(TakeInBall(robot.intake))
		self.btn4.whileHeld(PushOutBall(robot.intake))
	def getJoystick(self):
		return self.joy

	def getLiftstick(self):
		return self.joy_lift
