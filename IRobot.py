import socket
import thread
import sys

class IRobot:
	def __init__(self,host,port):
		self.posx = 0
		self.posy = 0
		self.posz = 0
		self.r = 0
		self.p = 0
		self.y = 0
		self.name = ''
		self.USARconnect(host,port)
		self.stringBuffer = ''
		

	def USARconnect(self,host,port):
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.connect((host,int(port)))
		self.stringBuffer = self.s.recv(1024)

	def SendCommand(self,command):
		if command == 'INIT':
			self.s.send('INIT {ClassName USARBot.AIRRobot} {Location 0,0000, 0,0000, 0,0000} {Rotation 0,0000, 0,0000, 0,0000}\r\n')
			self.stringBuffer = self.s.recv(1024)
			
	def RobotEngine(self):
		pass

 	
	
