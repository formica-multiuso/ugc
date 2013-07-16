import socket
import threading
import sys
from GamebotsParser import *

class IRobot:
	def __init__(self,host,port,name):
		self.posx = 0
		self.posy = 0
		self.posz = 0
		self.r = 0
		self.p = 0
		self.y = 0
		self.name = name
		self.USARconnect(host,port)
		self.parse = GamebotsParser(self.s,name)
		self.parse.start()

	def USARconnect(self,host,port):
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.connect((host,int(port)))

	def SendCommand(self,command,param_list):
		if command == 'AIRRobot INIT':
			self.s.send('INIT {ClassName USARBot.AIRRobot} {Location 0,0000, 0,0000, 0,0000} {Rotation 0,0000, 0,0000, 0,0000}\r\n')
		if command == 'AIRRobot DRIVE AltitudeVel':	
			self.s.send('DRIVE {AltitudeVelocity ' + param_list[0] + '}\r\n')
		
		if command == 'AIRRobot DRIVE RotationalVel':
			self.s.send('DRIVE {RotationalVelocity ' + param_list[0] + '}\r\n')	
		
		if command == 'AIRRobot DRIVE LinearVel':
			self.s.send('DRIVE {LinearVelocity ' + param_list[0] + '}\r\n')

	def RobotEngine(self):
		pass

 	
	
