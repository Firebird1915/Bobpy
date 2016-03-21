import wpilib
from wpilib.command import Subsystem

class Intake(Subsystem):
    """docstring for intake"""

    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        rate = 24/0.9

        self.rightin_1 = wpilib.CANTalon(7)
        self.rightin_1.changeControlMode(wpilib.CANTalon.ControlMode.Speed)
        self.rightin_1.setVoltageRampRate(rate)
        self.rightin_1.reverseOutput(True)




        '''Put all the intake Talons together in one drivesystem'''
        '''This idea was lame and made it harder for me to adjust'''
        # self.motor_intake = wpilib.RobotDrive(self.rightin_1,
        #                                       self.leftin_1)
    def takeball(self):
        self.rightin_1.set(300*360)

    def loseball(self):
        self.rightin_1.set(-100*360)
