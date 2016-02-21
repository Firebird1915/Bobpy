import wpilib 
from wpilib.command import Subsystem

class Intake(Subsystem):
    """docstring for intake"""
    
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.rightin_1 = wpilib.CANTalon(8)
        self.rightin_2 = wpilib.CANTalon(9)
        self.leftin_1 = wpilib.CANTalon(10)
        self.leftin_2 = wpilib.CANTalon(11)

        '''Put all the intake Talons together in one drivesystem'''
        self.motor_intake = wpilib.RobotDrive(self.rightin_1,
                                              self.rightin_2,
                                              self.leftin_1,
                                              self.leftin_2)



    def takeball(self):
        self.motor_intake.drive(1,-1)

    def loseball(self):
        self.motor_intake.drive(1,1)