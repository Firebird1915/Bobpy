import wpilib
from wpilib.command import Subsystem
from commands.lift_arm import MoveArm

class LiftMech(Subsystem):
    """ The arm works with only one motor gearbox with
        a 10:1 gear ratio.
    """
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.armMotor = wpilib.CANTalon(12)

        self.armMotor.changeControlMode(wpilib.CANTalon.ControlMode.Position)

        self.armMotor.setFeedbackDevice(wpilib.CANTalon.FeedbackDevice.QuadEncoder)

        self.armMotor.setPID(1.0,0.0,0.0)

        self.armMotor.setVoltageRampRate(24.0/0.9)
        self.sd = wpilib.SmartDashboard

        self.limitsiwtch = wpilib.DigitalInput(0)

    def initDefaultCommand(self):
        self.setDefaultCommand(MoveArm(self.robot))

    def Moveup(self):
        '''
            This in theory will lift the arm to the top of the robot
        '''
        self.armMotor.changeControlMode(wpilib.CANTalon.ControlMode.Position)
        self.armMotor.setPosition(-2000)

    def moveDown(self):
       self.armMotor.changeControlMode(wpilib.CANTalon.ControlMode.Position)
       self.armMotor.setPosition(4100)

    def stopmovement(self):
        self.armMotor.set(0)


    def limitPOS(self):
        if self.armMotor.getEncPosition() <= -2729.00: #421.000
            self.armMotor.changeControlMode(wpilib.CANTalon.ControlMode.PercentVbus)
            self.armMotor.set(0)
            return True
        elif self.armMotor.getEncPosition() >= 4999:
            self.armMotor.changeControlMode(wpilib.CANTalon.ControlMode.PercentVbus)            
            self.armMotor.set(0)
            return True
        else:
            return False

    def limitme(self):
        if self.limitPOS() == True and self.armMotor.getEncPosition() <= -2729.00:
            self.Moveup()
        elif self.limitPOS() == True and self.armMotor.getEncPosition() >= 4999:
            self.moveDown()

    def moveref(self, joy_lift):

        if joy_lift.getRawAxis(1) == -1 and self.limitsiwtch.get() == True:
            self.armMotor.changeControlMode(wpilib.CANTalon.ControlMode.PercentVbus)
            self.armMotor.set(joy_lift.getRawAxis(1)*0.4)
        elif joy_lift.getRawAxis(1) == 1 and self.limitsiwtch.get() == True:
            self.armMotor.changeControlMode(wpilib.CANTalon.ControlMode.PercentVbus)
            self.armMotor.set(joy_lift.getRawAxis(1)*0.4)
        elif joy_lift.getRawAxis(1) == 1 and self.limitsiwtch.get() == False:
            self.armMotor.changeControlMode(wpilib.CANTalon.ControlMode.PercentVbus)
            self.armMotor.set(0)
        elif joy_lift.getRawAxis(1) == -1  and self.limitsiwtch.get() == False:
            self.armMotor.changeControlMode(wpilib.CANTalon.ControlMode.PercentVbus)
            self.armMotor.set(joy_lift.getRawAxis(1)*0.4) 
        else:
            self.armMotor.changeControlMode(wpilib.CANTalon.ControlMode.Voltage)
            self.armMotor.set(-0.300)
            self.limitme()


    def log(self):
        self.sd.putDouble("Arm Voltage", self.armMotor.getOutputVoltage())
        self.sd.putDouble("Arm Distance", self.armMotor.getEncPosition())
        self.sd.putDouble("Arm Current", self.armMotor.getOutputCurrent())
        self.sd.putBoolean("limitsiwtch", self.limitsiwtch.get())