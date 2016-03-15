#!/usr/bin/env python3

import wpilib
from wpilib.command import Scheduler
from networktables import NetworkTable
import logging
from oi import OI

from subsystems.drivetrain import DriveTrain
from subsystems.pneumatics_comp import Pneumatics
from subsystems.intake import Intake
from subsystems.lift import LiftMech

class Bob(wpilib.IterativeRobot):

<<<<<<< HEAD
	#: update every 0.005 seconds/5 milliseconds (200Hz)
	kUpdatePeriod = 0.005

	def robotInit(self):
		"""
		This function is called upon program startup and
		should be used for any initialization code.
		"""
		self.drivetrain = DriveTrain(self)
		self.oi = OI(self)
		self.sd = NetworkTable.getTable("SmartDashboard")


		
	def autonomousInit(self): #has nothing so far probably wont who knows

		self.auto_loop_counter = 0 #teaches the roboto how to count

	def autonomousPeriodic(self):
		"""This function is called periodically during autonomous."""
		timer = wpilib.timer()
		timer.start()

		if self.auto_loop_counter < 100:
		    self.drive.drive(-0.5, 0) #drive forward
		    self.drive2.drive(-0.5,0)
		    self.auto_loop_counter += 1
		else:
		    self.robot_drive.drive(0,0)
		

	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""
		#cancel out autonomous
		while self.isOperatorControl() and self.isEnabled():

			Scheduler.getInstance().run()
			self.log()
		

	def testPeriodic(self):
		"""This function is called periodically during test mode."""
		wpilib.LiveWindow.run()

	def log(self):
		self.drivetrain.log()
		self.sd.putNumber('someNumber', 1234)
=======
    #: update every 0.005 seconds/5 milliseconds (200Hz)
    kUpdatePeriod = 0.005

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.drivetrain = DriveTrain(self)
        self.pneumatics_comp = Pneumatics(self)
        self.intake = Intake(self)
        self.lift = LiftMech(self)
        self.oi = OI(self)
        self.sd = NetworkTable.getTable("SmartDashboard")

        self.timer = wpilib.Timer()
        self.timer

        self.drivetrain.drive.setExpiration(0.1)
        self.drivetrain.drive2.setExpiration(0.1)
        self.drivetrain.drive.setSafetyEnabled(True)
        self.drivetrain.drive2.setSafetyEnabled(True)



        
    def autonomousInit(self): #has nothing so far probably wont who knows
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        self.drivetrain.drive.setSafetyEnabled(False)
        self.drivetrain.drive2.setSafetyEnabled(False)
        if self.auto_loop_counter < 240:
            self.drivetrain.drive.tankDrive(-0.8, -0.8) #drive forward
            self.drivetrain.drive2.tankDrive(-0.8, -0.8)
            self.auto_loop_counter += 1
        else:
            self.drivetrain.drive.tankDrive(0,0)
            self.drivetrain.drive2.tankDrive(0,0)
            self.drivetrain.drive.setSafetyEnabled(True)
            self.drivetrain.drive2.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        #cancel out autonomous
        while self.isOperatorControl() and self.isEnabled():

            Scheduler.getInstance().run()
            self.log()
        

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

    def log(self):
        self.drivetrain.log()
        self.lift.log()
        self.intake.log()
        self.sd.getBoolean('right trigger', self.oi.btn2.get())
        #self.sd.getBoolean('Right trigger?',self.r_trig.get())
>>>>>>> f2de1de593359f650e64fd224a5ad22e4d81745a


if __name__ == "__main__":
    wpilib.run(Bob)
