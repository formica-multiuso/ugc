import sys
import socket
import threading
from IRobot import IRobot

class AIRRobot(IRobot,threading.Thread):
	def __init__(self,host,port):
		threading.Thread.__init__(self)
		IRobot.__init__(self,host,port)
	
	def RobotEngine(self):
		pass

	def run(self):
		IRobot.SendCommand(self,"INIT")
		while 1:
			pass



