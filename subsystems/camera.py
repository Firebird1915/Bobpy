import wpilib
from wpilib.command import Subsystem

class Camera(Subsystem):
	"""docstring for CamCommand"""
	def __init__(self, robot):
		super().__init__()
		self.robot = robot
		self.camera = wpilib.USBCamera()
		self.camera.setExposureManual(50)
		self.camera.setBrightness(80)
		self.camera.updateSettings()

		server = wpilib.CameraServer.getInstance()
		server.startAutomaticCapture(self.camera)