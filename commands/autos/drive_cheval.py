import wpilib
from wpilib.command.commandgroup import CommandGroup

# Some commands we will need for this
from commands.simiautos.move_off_light import MoveOffLight
from commands.simiautos.armup import armUp
from commands.simiautos.armdown import armDown
from commands.autos.drive_forward_half import driveforward_half

class drive_Cheval(CommandGroup):
    """
        Command moves up to Cheval de frise
        lowers lift
        moves up a tad bit
        raises lift and moves forward
    """
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        addSequential(MoveOffLight(robot))
        addSequential(armDown(robot))
        addParallel(armUp(robot))
        addSequential(driveforward_half(robot))
