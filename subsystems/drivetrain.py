import wpilib
from wpilib.command import Subsystem
from networktables import NetworkTable
from commands.tankdrive_with_joystick import TankDriveWithJoystick

class DriveTrain(Subsystem):
    '''The DriveTrain system holds all the inital calls for the motors this includes 
        encoders as well. If you need to mess with the motors in the drive here is the spot.
    '''

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        

        self.l_motor1 = wpilib.CANTalon(1)
        self.l_motor2 = wpilib.CANTalon(2)
        self.l_motor3 = wpilib.CANTalon(3)

        self.l_motor1.reverseOutput(True)
        self.l_motor2.reverseOutput(True)
        self.l_motor3.reverseOutput(True)

        self.r_motor1 = wpilib.CANTalon(4)
        self.r_motor2 = wpilib.CANTalon(5)
        self.r_motor3 = wpilib.CANTalon(6)

        self.r_motor1.reverseOutput(True)
        self.r_motor2.reverseOutput(True)
        self.r_motor3.reverseOutput(True)

        #Compressor starts from the drivetrain but this all might change
        if self.isReal():
            self.compressor = wpilib.Compressor()
            self.compressor.start()
        
        self.switcher = wpilib.DoubleSolenoid(0,1)
        self.shifter = False            

        #Encoder talons from testbed
        #self.motor1 = wpilib.CANTalon(8) #initialize the motor as a Talon on channel 1
        #self.motor2 = wpilib.CANTalon(2)

        
        self.drive = wpilib.RobotDrive(self.l_motor1, # Tells the robot to call the tank drive method
                                       self.l_motor2,
                                       self.r_motor1,
                                       self.r_motor2) # Alternatively can use two stick method later on

        self.drive2= wpilib.RobotDrive(self.l_motor3,self.r_motor3)


        self.motor_encoder = wpilib.Encoder(0,1) # position of these two motors
        #block for eventual test simulation (see docs)
        self.sd = wpilib.SmartDashboard

    def initDefaultCommand(self):
        ''' If i didn't tell you to do something else
            you should let me drive
        '''
        self.setDefaultCommand(TankDriveWithJoystick(self.robot))


    def driveManual(self,left,right):
        '''Tank style driving
        '''
        self.drive.tankDrive(left,right)
        self.drive2.tankDrive(left,right)

    def driveJoystick(self, joy):
        ''' using a controller to drive tank style '''
        self.drive.tankDrive(joy.getRawAxis(1)/1.2, joy.getRawAxis(5)/1.2)
        self.drive2.tankDrive(joy.getRawAxis(1)/1.2,joy.getRawAxis(5)/1.2)
    
    def shiftFast(self):
        self.switcher.set(2)
        self.shifter = True

    def shiftReturn(self):
        self.switcher.set(0)
        self.shifter = False

    def is_shifted(self):
        return self.shifter

    def reset(self):
        ''' reset the encoders '''
        self.motor_encoder.reset()

    def log(self):
        # self.sd.putDouble("Encoder Distance", self.motor1.getEncPosition())
        # self.sd.putDouble("Big Encoder", self.motor1.getEncPosition()*2)
        pass