#!/usr/bin/env python3

import wpilib
from wpilib.command import Scheduler
from networktables import NetworkTable
import logging
from oi import OI

from commands.autos.drive_forward_static import driveforward_static
from commands.autos.drive_forward_underpass import driveforward_underpass
from commands.autos.drive_cheval import drive_Cheval

from subsystems.drivetrain import DriveTrain
from subsystems.pneumatics_comp import Pneumatics
from subsystems.intake import Intake
from subsystems.lift import LiftMech

class Bob(wpilib.IterativeRobot):

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

        self.drivetrain.drive.setExpiration(0.1)
        self.drivetrain.drive2.setExpiration(0.1)
        self.drivetrain.drive.setSafetyEnabled(True)
        self.drivetrain.drive2.setSafetyEnabled(True)


        self.autochooser = wpilib.SendableChooser()
        self.autochooser.addObject('DUKEBOYS',driveforward_static(self))
        self.autochooser.addObject('Underpass',driveforward_underpass(self))
        self.autochooser.addObject('Cheval de Frise (beta)',drive_Cheval(self))
        self.autochooser.addDefault('DUKEBOYS',driveforward_static(self))
        wpilib.SmartDashboard.putData("Autonomous Mode", self.autochooser)

        self.autoCommand = None




    def autonomousInit(self): #has nothing so far probably wont who knows
        # self.auto_loop_counter = 0
        self.autoCommand = self.autochooser.getSelected()
        self.autoCommand.start()

    def autonomousPeriodic(self):
        # """This function is called periodically during autonomous."""

        # self.drivetrain.drive.setSafetyEnabled(False)
        # self.drivetrain.drive2.setSafetyEnabled(False)
        # if self.auto_loop_counter < 240:
        #     self.drivetrain.drive.tankDrive(-0.8, -0.8) #drive forward
        #     self.drivetrain.drive2.tankDrive(-0.8, -0.8)
        #     self.auto_loop_counter += 1
        # else:
        #     self.drivetrain.drive.tankDrive(0,0)
        #     self.drivetrain.drive2.tankDrive(0,0)
        #     self.drivetrain.drive.setSafetyEnabled(True)
        #     self.drivetrain.drive2.setSafetyEnabled(True)
        Scheduler.getInstance().run()
        self.log()

    def teleopInit(self):
        if self.autoCommand is not None:
            self.autoCommand.cancel()

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
        self.sd.getBoolean('right trigger', self.oi.btn2.get())
        #self.sd.getBoolean('Right trigger?',self.r_trig.get())

if __name__ == "__main__":
    wpilib.run(Bob)
