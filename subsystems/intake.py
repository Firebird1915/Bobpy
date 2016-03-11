import wpilib 
from wpilib.command import Subsystem

class Intake(Subsystem):
    """docstring for intake"""
    
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        rate = 24/0.10
        self.rightin_1 = wpilib.CANTalon(7)
        self.rightin_1.setVoltageRampRate(rate)
        
        self.leftin_1 = wpilib.CANTalon(8)
        self.leftin_1.setVoltageRampRate(rate)
        self.leftin_1.reverseOutput(True)

        self.mechin = wpilib.CANTalon(9)
        self.mechin.changeControlMode(wpilib.CANTalon.ControlMode.Follower)

        fullspeed = False


        '''Put all the intake Talons together in one drivesystem'''
        self.motor_intake = wpilib.RobotDrive(self.rightin_1,
                                              self.leftin_1)




    def takeball(self):
        self.motor_intake.drive(1,-1)
        self.mechin.set(self.rightin_1.getDeviceID())

    def loseball(self):
        self.motor_intake.drive(1,1)
        self.mechin.set(self.rightin_1.getDeviceID())


    def windup(self):
        self.motor_intake.drive(1,1)

    def windcheck(self):
        return fullspeed 

    def log(self):
        pass
