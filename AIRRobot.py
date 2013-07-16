import sys
import socket
import threading
import time
from IRobot import IRobot

class AIRRobot(IRobot,threading.Thread):
	def __init__(self,host,port,name):
		threading.Thread.__init__(self)
		IRobot.__init__(self,host,port,name)
		self.name = name
	
	def RobotEngine(self):
		pass

	def run(self):
		IRobot.SendCommand(self,"AIRRobot INIT",[])
		time.sleep(5)	
		IRobot.SendCommand(self,"AIRRobot DRIVE AltitudeVel",['1'])
		time.sleep(5)
		IRobot.SendCommand(self,"AIRRobot DRIVE AltitudeVel",['0'])
		time.sleep(5)
		IRobot.SendCommand(self,"AIRRobot DRIVE LinearVel",['1'])
		time.sleep(5)
		IRobot.SendCommand(self,"AIRRobot DRIVE LinearVel",['-1'])
		time.sleep(5)
		IRobot.SendCommand(self,"AIRRobot DRIVE LinearVel",['1'])
		time.sleep(5)





