import wpilib

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.motor = wpilib.Jaguar(1)