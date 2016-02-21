import wpilib
from wpilib.command import Subsystem
from commands.speed_toggle import SpeedToggle

class Pneumatics(Subsystem):
    """docstring for Pneumatics"""
    kFwd = wpilib.DoubleSolenoid.Value.kFowoward
    kOff = wpilib.DoubleSolenoid.Value.kOff
    kReverse = wpilib.DoubleSolenoid.Value.kReverse

    def __init__(self, robot):
        super().__init__()
        self.comp = robot

        #Compressor starts from the drivetrain but this all might change
        if self.robot.isReal():
            self.compressor = wpilib.Compressor()
            self.compressor.start()
        
        self.switcher = wpilib.DoubleSolenoid(1,2)
        self.shifter = False   

    #turbo mode
    def shiftFast(self):
        self.switcher.set(1)
        self.shifter = True

    #cruise mode
    def shiftReturn(self):
        self.switcher.set(0)
        self.shifter = False

    #did we change speeds?
    def is_shifted(self):
        return self.shifter
