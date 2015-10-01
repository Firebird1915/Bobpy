import wpilib
from pyfrc.physics.drivetrains import mecanum_drivetrain
from hal_impl.data import hal.data

class PhysicsEngine:
	def __init__(self, r_stick, l_stick):
		self.stick1 = r_stick
		self.stick2 = l_stick

	def initialize(self, hal_data):
		hal_data['CAN'][1]['value'] = True
		hal_data['CAN'][2]['value'] = True
		hal_data['CAN'][3]['value'] = True
		hal_data['CAN'][4]['value'] = True


	def update_sim(self, hal_data, now, tm_diff):

		lf_motor = hal_data['CAN'][1]['value']
		lb_motor = hal_data['CAN'][1]['value']
		rf_motor = hal_data['CAN'][1]['value']
		rb_motor = hal_data['CAN'][1]['value']

