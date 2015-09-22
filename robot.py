#!/usr/bin/env python3
'''
    This sample program shows how to control a motor using a joystick. In the
    operator control part of the program, the joystick is read and the value
    is written to the motor.
    Joystick analog values range from -1 to 1 and speed controller inputs also
    range from -1 to 1 making it easy to work together. The program also delays
    a short time in the loop to allow other threads to run. This is generally
    a good idea, especially since the joystick values are only transmitted
    from the Driver Station once every 20ms.
'''
import wpilib

class Bob(wpilib.SampleRobot):
    
    #: update every 0.005 seconds/5 milliseconds (200Hz)
    kUpdatePeriod = 0.005

    def robotInit(self):
        '''Robot initialization function'''
        
        self.motor1 = wpilib.CANTalon(2)        # initialize the motor as a Talon on channel 1
        self.motor2 = wpilib.CANTalon(3)   
        
        self.motor3 = wpilib.CANTalon(4).reverseOutput(True)    #reverses the motor set so that it goes into the right direction
        self.motor4 = wpilib.CANTalon(1).reverseOutput(True)
        
        self.stick = wpilib.Joystick(0)     # initialize the joystick on port 0
        self.stick2 = wpilib.Joystick(1)    # initialize the joystick on port 1

        self.switch = wpilib.DigitalInput(9)
        self.piston1 = wpilib.DoubleSolenoid(0,1)
        self.encoder1 = wpilib.Encoder(0,1)


        if self.isReal():
           self.compressor = wpilib.Compressor()
           self.compressor.start() 

    def autonomous(self):
        '''Called when autonomous mode is enabled.'''

        while self.isAutonomous() and self.isEnabled():
            wpilib.Timer.delay(0.01)

    def operatorControl(self):
        '''Runs the motor from a joystick.'''
        while self.isOperatorControl() and self.isEnabled():
            
            # Set the motor's output.
            # This takes a number from -1 (100% speed in reverse) to
            # +1 (100% speed going forward)
            
            self.motor2.setFeedbackDevice()

            #Enables the dashboard to show the boolean of the object
            wpilib.SmartDashboard.putBoolean('Limit Switch', self.switch.get())
            wpilib.SmartDashboard.putBoolean('Compressor', self.compressor.enabled())
            wpilib.SmartDashboard.putBoolean('TRIGGER', self.stick.getTrigger())

            #Still have no idea how this worked
            wpilib.SmartDashboard.putNumber('Encoder Distance', self.motor2.getEncPosition())

            #reacts to joystick0
            self.motor1.set(self.stick1.getY())
            self.motor2.set(self.stick1.getY())

            #reacts to joystick1
            self.motor3.set(self.stick2.getY())
            self.motor4.set(self.stick2.getY())

            if self.stick.getTrigger():
                self.piston1.set(1)
            else:
                self.piston1.set(2)

            wpilib.Timer.delay(self.kUpdatePeriod)  # wait 5ms to the next update
            


if __name__ == "__main__":
    wpilib.run(Bob)
